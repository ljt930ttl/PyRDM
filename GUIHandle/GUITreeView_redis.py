#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 10:47
@Author:  linjinting
@File: GUITreeView_redis.py
@Software: PyCharm
"""

from PyQt5.QtWidgets import QTreeView, QAbstractItemView
from GUIHandle.communicate import bus

from modules.redis_model import RedisTreeModel
from global_config import mapServer
from operator_factory import OperatorFactory
from redis_connection_base import RedisConnectionBase

class RedisTreeView(QTreeView):
    # clientItem = pyqtSignal

    def __init__(self):
        super(RedisTreeView, self).__init__()
        ## set property
        self.keys_data = None

        self.setHeaderHidden(True)
        self.setItemsExpandable(True)
        self.resizeColumnToContents(0)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.model_ = RedisTreeModel()

        self.initSingle()

    def initSingle(self):
        # init single
        self.clicked.connect(self.clikedTreeItem)
        bus.createServerItem.connect(self.createServerItem)

    def createServerItem(self, conf):
        # print(arg)
        serve_name = conf.get('name', None)
        if serve_name is None:
            return

        self.model_.setupData({'name': serve_name, 'type': 'server', 'config': conf, 'status': 0})  ###
        self.setModel(self.model_)

    def createDB(self, item):
        item.changeItemStatus(1)
        self.model_.setupData({'name': 'db0', 'type': 'db', 'count': len(self.keys_data)}, item=item)

    def clikedTreeItem(self, index):
        # print(index)
        # model_ = self.model()
        item = self.model_.getItemFromIndex(index)
        if item.itemType() == 'server' and item.itemStatus() == 0:
            item.changeItemStatus(1)
            conf = item.itemConfig()
            if self.connServer(conf):
                # create DB Item
                self.model_.setupData(
                    {'name': 'db0', 'type': 'db', 'config': conf, 'status': 0, 'count': len(self.keys_data)}, item=item)
                item.changeItemStatus(1)
                self.setExpanded(index, True)
            else:
                item.changeItemStatus(0)

        if item.itemType() == 'db':
            # create Keys Item
            self.model_.setupData(
                {'name': 'db0', 'type': 'keys', 'config': item.itemConfig(), 'data': self.keys_data}, item=item)
            self.setExpanded(index, True)

        if item.itemType() == 'key':
            # create value container
            bus.clickedKeyItem.emit(item.itemData)

    def connServer(self, conf):
        redis_pool = RedisConnectionBase(conf['config'])
        conn = redis_pool.get_conn()
        if conn is None:
            print('conneciton error')
            return False

        factory = OperatorFactory(conn)

        opera = factory.createOperator('redis')

        try:
            self.keys_data = opera.scan()
            mapServer[conf['name']] = conn
            return True
        except Exception as e:
            print(e)
            return False
