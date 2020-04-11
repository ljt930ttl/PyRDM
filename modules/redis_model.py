#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/1 13:37
@Author:  linjinting
@File: redis_model.py
@Software: PyCharm
"""

from PyQt5 import QtWidgets
from PyQt5 import QtCore
from modules.items.redis_item import RedisItem, ServerItem, DBItem, NamespaceItem, KeyItem
from utils.chars_proc import RedisNamespaceSplit

class TreeModel(QtCore.QAbstractItemModel):
    def __init__(self, parent=None):
        super(TreeModel, self).__init__(parent)
        self.rootItem = RedisItem()
    def setupData(self,*args):
        #初始化
        pass

    def columnCount(self, parent=None, *args, **kwargs):
        # return 1
        if parent.isValid():
            return parent.internalPointer().columnCount()
        else:
            return self.rootItem.columnCount()

    def data(self, index, role=None):

        if not index.isValid():
            return None
        if role != QtCore.Qt.DisplayRole:
            return None
        item = index.internalPointer()
        return item.data(index.column())

    def setData(self, index, data, role=None):

        # 编辑后更新模型中的数据 View中编辑后，View会调用这个方法修改Model中的数据
        if index.isValid() and data:
            col = index.column()
            print(col)
            # if 0 < col < len(self.headers):
            # self.beginResetModel()
            item = index.internalPointer()
            # print(data)
            item.itemData = data
            # if CONVERTS_FUNS[col]:  # 必要的时候执行数据类型的转换
            #     self.datas[index.row()][col] = CONVERTS_FUNS[col](value)
            # else:
            #     self.datas[index.row()][col] = value
            self.dirty = True
            self.dataChanged.emit(index,index)
            return True
        return False

    # def dataChanged(self, QModelIndex, QModelIndex_1, roles, p_int=None, *args, **kwargs):
    #     print(QModelIndex, QModelIndex_1, roles)
    #     print(p_int=None, *args, **kwargs)

    def flags(self, index):
        # if not index.isValid():
        #     return QtCore.Qt.NoItemFlags
        #
        # return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        ###QtCore.Qt.ItemIsEditable #可编辑
        return  QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.DragMoveCursor

    def headerData(self, section, orientation, role=None):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.rootItem.data(section)

        return None

    def index(self, row, column, parent=None, *args, **kwargs):
        if not self.hasIndex(row, column, parent):
            return QtCore.QModelIndex()

        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        else:
            return QtCore.QModelIndex()

    def parent(self, index=None):
        if not index.isValid():
            return QtCore.QModelIndex()

        childItem = index.internalPointer()
        parentItem = childItem.parent()

        if parentItem == self.rootItem:
            return QtCore.QModelIndex()

        return self.createIndex(parentItem.row(), 0, parentItem)

    def rowCount(self, parent=None, *args, **kwargs):
        # if parent.column() > 0:
        #     return 0
        if not parent.isValid():
            parentItem = self.rootItem
        else:
            parentItem = parent.internalPointer()

        return parentItem.childCount()
    def getIndexFromItem(self,childItem):

        if childItem:
            row = childItem.row()
            return self.createIndex(row, 0, childItem)
        else:
            return QtCore.QModelIndex()

    def getItemFromIndex(self,index):
        if index :
            return index.internalPointer()

    def mimeData(self, indexes, QModelIndex=None):
        item = self.getItemFromIndex(indexes[0])
        print(item.itemData)
        mimedata = QtCore.QMimeData()
        mimedata.setData('text',b"t")
        mimedata.setImageData(indexes[0])
        return mimedata

class RedisTreeModel(TreeModel):
    def __init__(self, parent=None):
        super(RedisTreeModel,self).__init__(parent=parent)
        self.data = None
        self.namespace_map = dict()

    def setupServer(self, data, item=None):
        if data.get('type',None) == 'server':
            _item = self.rootItem.mapItems.get(data['name'], None)
            if _item is None:
                server_item = ServerItem(self.__createItemData(**data), self.rootItem)
                self.insertRow(server_item.row())
                self.rootItem.appendChild(server_item)
                self.rootItem.mapItems[data['name']] = server_item
                # index = self.getIndexFromItem(server_item)
                # self.setData(index, self.__createItemData(**data))
            else:
                ## 不允许重名服务
                return


        elif data.get('type',None) == 'db' and item is not None:
            name = 'db0' ## 暂时创建一个
            db_item = DBItem(self.__createItemData(**data),  item)
            item.appendChild(db_item)
            item.mapItems[name] = db_item
        else:
            raise TypeError('data type error')

    def setupData(self, data, item=None):
        self.data = data
        if data.get('type', None) == 'server':
            _item = self.rootItem.mapItems.get(data['name'], None)
            if _item is None:
                server_item = ServerItem(parent=self.rootItem)

                self.rootItem.appendChild(server_item)
                self.rootItem.mapItems[data['name']] = server_item
                index = self.getIndexFromItem(server_item)
                self.setData(index,self.__createItemData(**data) )

                return server_item
                # print('xx')
            else:
                ## 不允许重名服务
                return
        elif data.get('type', None) == 'db' and item is not None:
            name = 'db0'  ## 暂时创建一个
            db_item = DBItem(self.__createItemData(**data), item)
            item.appendChild(db_item)
            item.mapItems[name] = db_item

        elif data.get('type', None) == 'keys':
            # item = self.server_item.mapItems.get(DB, None)

            if item is None:
                print('item error')
                return

            data_ = sorted(data['data'])
            print("%s start" % (get_time_stamp()))
            for full_name in data_:
                # print(full_name,count)
                full_name = bytes.decode(full_name)
                self._renderLazily(item, full_name, full_name)
                # count -=1
            print("%s end"%(get_time_stamp()))
        else:
            raise TypeError('data type error')



    def _renderLazily(self,parent_item, full_name, remainder_name):
        # print("name:%s in level:%d"%(full_name,level))
        name_list = RedisNamespaceSplit.split_namespace(remainder_name)
        if name_list == None:
            return
        else:
            if len(name_list) > 1:
                node_name = name_list[0]
                remainder_name = name_list[1]
                type_ = "namespace"
            else:
                node_name = full_name
                remainder_name = ""
                type_ = "key"
        # if node_name == "test":
        #     print(node_name)

            # map_obj = parent_item.mapItems

        _item = parent_item.mapItems.get(node_name, None)
        # _item = self.getItemFromNode(node_level)
        child_item = None
        if _item is not None:
            if  _item.itemData['type'] == type_:
                child_item = _item ##

        if child_item is None:
            # _node =  {'name': node_name, 'count': count}
            if type_ == 'namespace':
                child_item = NamespaceItem(
                    self.__createItemData(name=node_name, type=type_, config=self.data['config']), parent_item)
            else:
                child_item = KeyItem(
                    self.__createItemData(name=node_name, type=type_, config=self.data['config']), parent_item)

            parent_item.appendChild(child_item)
            # _index = self.getIndexFromItem(new_item)
            parent_item.mapItems[node_name] = child_item  # 利用字典，存储node与item的对应关系
            # self.namespace_map[node_level] = self.getIndexFromItem(child_item) #利用 TreeItem 存储，查找index会非常慢


        if remainder_name == "":
            return

        self._renderLazily(child_item, full_name, remainder_name)

    def __createItemData(self, **kwargs):
        return kwargs

    def getItemName(self,Item):
        return Item.itemData


import time
def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

if __name__ == '__main__':
    import sys
    import get_data

    data = get_data.get_all_keys()


    model = RedisTreeModel()
    model.setupData(data) ###

    app = QtWidgets.QApplication(sys.argv)
    view = QtWidgets.QTreeView()
    view.setModel(model)
    view.setHeaderHidden(True)

    view.setItemsExpandable(True)
    view.resizeColumnToContents(0)
    view.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
    view.setWindowTitle("Simple Tree Model")

    view.show()
    sys.exit(app.exec_())