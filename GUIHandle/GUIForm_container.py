#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/2 11:42
@Author:  linjinting
@File: GUIForm_container.py
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget,QTableWidgetItem,QTableWidget
from UI.ui_tabWidget_container import Ui_tabWidgetContainer
from GUIHandle.communicate import bus

import json
from global_config import mapServer



class FormContainer(QWidget, Ui_tabWidgetContainer):
    def __init__(self):
        super(FormContainer,self).__init__()
        self.setupUi(self)
        bus.clickedKeyItem.connect(self.showKeys)
        # self.handle = RedisConneciton()

        self.tableWidget_values.doubleClicked.connect(self.showValue)
        self.pushButton_save.clicked.connect(self.updateValue)

        self.opera = None

    def showKeys(self,itemData):
        conn = mapServer.get(itemData['config']['name'], None)
        type_ , self.result, self.opera = conn.getData(itemData['name']) # 分割字符串的时候已经把key 转成str了 不需要再decode
        # print(result)
        fields = self.result.keys()
        self.createTable(fields)

        text_ = type_.decode().upper() + ":"
        self.label_keyType.setText(text_)
        self.lineEdit_keyTitle.setText(itemData['name'])
        self.label_field_count.setText(str(len(fields)))
        # values = result.values()

    def createTable(self,fields):
        r = 0
        self.tableWidget_values.setColumnCount(2)
        self.tableWidget_values.setRowCount(len(fields))
        self.tableWidget_values.setHorizontalHeaderLabels(['key', 'value'])
        self.tableWidget_values.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_values.setSelectionBehavior(QTableWidget.SelectRows)  # 整行选中的方式
        self.tableWidget_values.horizontalHeader().setStretchLastSection(True)
        #self.tableWidget_keys.resizeColumnsToContents()  # 将列调整到跟内容大小相匹配
        # self.tableWidget_keys.resizeRowsToContents()  # 将行大小调整到跟内容的大学相匹配
        for key in fields:
            newItem = QTableWidgetItem(key.decode())
            self.tableWidget_values.setItem(r, 0, newItem)
            newItem = QTableWidgetItem(self.result[key].decode())
            self.tableWidget_values.setItem(r, 1, newItem)
            r +=1

    def showValue(self):
        row = self.tableWidget_values.currentRow()
        self.field = self.tableWidget_values.item(row, 0).text()
        value = self.tableWidget_values.item(row, 1).text()
        # print(value)

        self.textEdit_key.setText(self.field)
        self.textEdit_value.setText(self.formatJson(value))

        self.label_field_size.setText(str(len(self.field)))
        self.label_valus_size.setText(str(len(value)))

    def updateValue(self):
        key_ = self.lineEdit_keyTitle.text()
        new_value = self.textEdit_value.toPlainText()
        new_field = self.textEdit_key.toPlainText()
        if new_field != self.field:
            self.opera.delData(key_, self.field)

        self.opera.update(key_, new_field, new_value)

    def formatJson(self,value):
        try:
            loads = json.loads(value)
            return json.dumps(loads, sort_keys=True, indent=4)
        except:
            return value


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    form = FormContainer()
    form.show()
    sys.exit(app.exec_())