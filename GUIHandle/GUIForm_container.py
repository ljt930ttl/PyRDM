#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/2 11:42
@Author:  linjinting
@File: GUIForm_container.py
@Software: PyCharm
"""
import json
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QTableWidget
from UI.ui_tabWidget_container import Ui_tabWidgetContainer
from UI.ui_QWdiget_key_container import Ui_QWidget_key_conntainer
from GUIHandle.communicate import bus

from operator_factory import OperatorFactory
from global_config import mapServer


def formatJson(value):
    try:
        loads = json.loads(value)
        return json.dumps(loads, sort_keys=True, indent=4)
    except:
        return value







class FormContainer(QWidget, Ui_tabWidgetContainer, Ui_QWidget_key_conntainer):
    def __init__(self):
        super(FormContainer, self).__init__()
        self.setupUi(self)
        bus.clickedKeyItem.connect(self.initKeyContainer)
        # self.handle = RedisConneciton()


        # self.tableWidget_values.doubleClicked.connect(self.showValue)
        # self.pushButton_save.clicked.connect(self.updateValue)

        self.opera = None

    def initKeyContainer(self, itemData):
        # server_name = itemData['config']['name']
        key_name = itemData['name']
        conn = mapServer.get(itemData['config']['name'], None)
        factory = OperatorFactory(conn)
        opera = factory.createOperator(key=key_name)
        self.result = opera.getData(key_name)  # 分割字符串的时候已经把key 转成str了 不需要再decode
        type_ = opera.opera_type.decode()

        self.tabKeyContainer = ZSetKeyContainer(key_name, self.result, type_)
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
    form = FormContainer()
    form.show()
    sys.exit(app.exec_())
