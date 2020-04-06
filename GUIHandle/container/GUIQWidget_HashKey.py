#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQWidget_HashKey.py
@time: 2020/4/6 10:49
'''

from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from GUIHandle.container.GUIQWidget_container_base import KeyContainerBase


class HashKeyContainer(KeyContainerBase):
    def __init__(self, key_name, values, type_):
        super(HashKeyContainer, self).__init__(key_name, values, type_)
        self.setupUi(self)
        self.field = None
        self.tableHeard = ['key', 'value']

        self.initData()

    def initData(self):
        fields = self.values.keys()
        self.setTitle(self.type_, self.key_name, fields)
        self.createTable(fields)
        self.tableWidget_values.doubleClicked.connect(self.displayValue)

    def setTitle(self, type_, key_name, fields):
        text_ = type_.upper() + ":"
        self.label_keyType.setText(text_)
        self.lineEdit_keyTitle.setText(key_name)
        self.label_fieldCount.setText(str(len(fields)))

    def createTable(self, fields):
        self.tableWidget_values.setColumnCount(2)
        self.tableWidget_values.setRowCount(len(fields))
        self.tableWidget_values.setHorizontalHeaderLabels(self.tableHeard)
        self.tableWidget_values.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_values.setSelectionBehavior(QTableWidget.SelectRows)  # 整行选中的方式
        self.tableWidget_values.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget_keys.resizeColumnsToContents()  # 将列调整到跟内容大小相匹配
        # self.tableWidget_keys.resizeRowsToContents()  # 将行大小调整到跟内容的大学相匹配
        self.setTableData(fields)

    def setTableData(self, fields):
        r = 0
        for key in fields:
            newItem = QTableWidgetItem(key.decode())
            self.tableWidget_values.setItem(r, 0, newItem)
            newItem = QTableWidgetItem(self.result[key].decode())
            self.tableWidget_values.setItem(r, 1, newItem)
            r += 1

    def displayField(self, row):
        self.field = self.__getTableField(row)  # 需要保持，方便后面判断
        self.textEdit_key.setText(self.field)
        self.label_fieldSize.setText(str(len(self.field)))

    def displayValue(self):
        row = self.tableWidget_values.currentRow()
        value = self.__getTableValue(row)  # ##
        self.textEdit_value.setText(value)
        self.label_valusSize.setText(str(len(value)))

        self.displayField(row)

    def __getTableValue(self, row):
        return self.tableWidget_values.item(row, 0).text()  # ##

    def __getTableField(self, row):
        return self.tableWidget_values.item(row, 1).text()

    def updateValue(self):
        key_ = self.lineEdit_keyTitle.text()
        new_value = self.textEdit_value.toPlainText()
        new_field = self.textEdit_key.toPlainText()
        if new_field != self.field:
            self.opera.delData(key_, self.field)

        self.opera.update(key_, new_field, new_value)
