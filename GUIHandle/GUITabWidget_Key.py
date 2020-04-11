#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/2 11:42
@Author:  linjinting
@File: GUITabWidget_Key.py
@Software: PyCharm
"""
import json
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QTableWidget
from UI.ui_tabWidget_container import Ui_tabWidgetContainer
from GUIHandle.container.GUIQWidget_HashKey import HashKeyContainer
from GUIHandle.container.GUIQwidget_ZSetKey import ZSetKeyContainer
from GUIHandle.container.GUIQWidget_SetKey import SetKeyContainer
from GUIHandle.container.GUIQWidget_ListKey import ListKeyContainer
from GUIHandle.container.GUIQWidget_StringKey import StringKeyContainer

from GUIHandle.communicate import bus

from operator_factory import OperatorFactory
from global_config import mapServer





class TabKeyContainer(QWidget, Ui_tabWidgetContainer):
    def __init__(self):
        super(TabKeyContainer, self).__init__()
        self.setupUi(self)
        bus.clickedKeyItem.connect(self.initKeyContainer)
        bus.containerReload.connect(self.initKeyContainer)
        # self.handle = RedisConneciton()

        # self.tableWidget_values.doubleClicked.connect(self.showValue)
        # self.pushButton_save.clicked.connect(self.updateValue)

        self.opera = None
        self.itemData = None

        self.container = {
            'hash': HashKeyContainer,
            'zset': ZSetKeyContainer,
            'set': SetKeyContainer,
            'list': ListKeyContainer,
            'string': StringKeyContainer,
        }

    def initKeyContainer(self, itemData=None):
        # server_name = itemData['config']['name']
        if itemData is None:
            if self.itemData is not None:
                itemData = self.itemData
            else:
                return

        self.itemData = itemData
        key_name = itemData['name']
        conn = mapServer.get(itemData['config']['name'], None)
        factory = OperatorFactory(conn)
        opera = factory.createOperator(key=key_name)
        self.result = opera.getData(key_name)  # 分割字符串的时候已经把key 转成str了 不需要再decode
        type_ = opera.opera_type.decode()
        ttl_ = opera.getKeyTTL(key_name)
        container_ = self.container.get(type_, None)

        self.tabKeyContainer = container_(key_name, self.result, ttl_, opera)
        self.tabKeyContainer.setObjectName('tabKeyContainer')
        self.tabWidget_container.addTab(self.tabKeyContainer, key_name)
        self.tabWidget_container.removeTab(0)
        self.tabWidget_container.setTabsClosable(True)

        # if type_ == 'hash' or type_ == 'zset':
        #     fields = self.result.keys()
        # self.tabKeyContainer.setTitle(type_, key_name, fields)
        # self.tabKeyContainer.createTable(fields)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    form = TabKeyContainer()
    form.show()
    sys.exit(app.exec_())
