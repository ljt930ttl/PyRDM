#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/1 12:14
@Author:  linjinting
@File: redis_item.py
@Software: PyCharm
"""
from modules.items.tree_item import TreeItem


class RedisItem(TreeItem):
    def __init__(self, data=None, parent=None):
        super(RedisItem, self).__init__(data)
        self.parentItem = parent
        self.itemData = data
        # self.values_list = list(data.values())
        self.childItems = []
        self.mapItems = dict()

    def appendChild(self, item):
        self.childItems.append(item)

    def updateMetedata(self, node, item):
        self.mapItems[node] = item

    def data(self, column):
        try:
            # return (self.getItemName(),self.getItemId(),self.getItemUid(),self.getItemCode())[column]
            # name = self.itemData.get('name', 0)
            type_ = self.itemType()
            if type_ == 'key':
                value = self.itemName()
            elif type_ == 'namespace':
                value = "%s (%d)" % (self.itemName(), self.childItemsCount())
            else:
                value = ""
            return value
        except IndexError:
            return None

    def childItemsCount(self):
        count = 0
        if len(self.childItems) == 0:
            return count + 1
        else:
            for item in self.childItems:
                count += item.childItemsCount()
            return count

    def itemType(self):
        return self.itemData.get('type', None)

    def itemName(self):
        return self.itemData.get('name', None)

    def itemConfig(self):
        return self.itemData.get('config', None)

class ServerItem(RedisItem):
    def data(self, column):
        try:
            value = self.itemName()
            return value
        except IndexError:
            return None

    ### server

    def itemStatus(self):
        return self.itemData.get('status', -1)

    def changeItemStatus(self, status):
        if self.itemData.get('status', -1) == -1:
            print("error")
        else:
            self.itemData['status'] = status

class DBItem(RedisItem):
    def data(self, column):
        try:
            value = "%s (%d)" % (self.itemName(), self.keysCount())
            return value
        except IndexError:
            return None
    ## db
    def keysCount(self):
        return self.itemData.get('count', 0)
