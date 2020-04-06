#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQwidget_ZSetKey.py
@time: 2020/4/6 10:56
'''
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from GUIHandle.container.GUIQWidget_container_base import KeyContainerBase


class ZSetKeyContainer(KeyContainerBase):
    def __init__(self, key_name, values, type_):
        super().__init__(key_name, values, type_)
        self.setupUi(self)

        # self.key_name = key_name
        # self.values = values
        # self.type_ = type_

        self.tableHeaders = ['value', 'source']
        self.initData()

    def initData(self):
        # fields = self.values

        self.setTitle(self.type_, self.key_name, self.values)
        self.createTable(self.values)

        self.tableWidget_values.doubleClicked.connect(self.displayValue)
        # self.displayValue()

    def createTable(self, fields):
        self.tableWidget_values.setColumnCount(2)
        self.tableWidget_values.setRowCount(len(fields))
        self.tableWidget_values.setHorizontalHeaderLabels(self.tableHeaders)
        self.tableWidget_values.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_values.setSelectionBehavior(QTableWidget.SelectRows)  # 整行选中的方式
        self.tableWidget_values.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget_keys.resizeColumnsToContents()  # 将列调整到跟内容大小相匹配
        # self.tableWidget_keys.resizeRowsToContents()  # 将行大小调整到跟内容的大学相匹配

        self.setTableData(fields)

    def setTableData(self, value):
        r = 0
        for value, source in value:
            newItem = QTableWidgetItem(value.decode())
            self.tableWidget_values.setItem(r, 0, newItem)
            newItem = QTableWidgetItem(str(source))
            self.tableWidget_values.setItem(r, 1, newItem)
            r += 1

    def setTitle(self, type_, key_name, values):
        text_ = type_.upper() + ":"
        self.label_keyType.setText(text_)
        self.lineEdit_keyTitle.setText(key_name)
        self.label_fieldCount.setText(str(len(values)))

    def displayField(self, row):
        source = self.__getTableField(row)
        self.textEdit_key.setText(source)
        # self.label_fieldSize.setText(str(len(source)))

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

    def __getNewData(self):
        new_value = self.textEdit_value.toPlainText()
        new_field = self.textEdit_key.toPlainText()
        return new_value, new_field

    def updateValue(self):
        new_value, new_field = self.__getNewData()
        if new_field != self.field:
            self.opera.delData(self.key_name, self.field)

        self.opera.update(self.key_name, new_field, new_value)