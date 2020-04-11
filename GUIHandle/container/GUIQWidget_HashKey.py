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
    def __init__(self, key_name, values, TTL,opera):
        super(HashKeyContainer, self).__init__(key_name, values, TTL,opera)
        # self.setupUi(self)
        self.field = None
        self.tableHeaders = ['key', 'value']
        self.type_ = 'hash'
        self.label_keyName = 'Key:'



        self.initData()

    def initData(self):
        fields = self.values.keys()
        self.setTitle(self.type_, self.key_name, fields)
        self.initDisplayArea()
        self.tableWidget_values.doubleClicked.connect(self.displayValue)


    def initDisplayArea(self):
        self.createTable(self.values)
        self.textEdit_key.setEnabled(False)
        self.textEdit_value.setEnabled(False)

    def createTable(self, fields):
        self.tableWidget_values.setColumnCount(2)
        self.tableWidget_values.setRowCount(len(fields))
        self.tableWidget_values.setHorizontalHeaderLabels(self.tableHeaders)
        self.tableWidget_values.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_values.setSelectionBehavior(QTableWidget.SelectRows)  # 整行选中的方式
        self.tableWidget_values.horizontalHeader().setStretchLastSection(True)
        r = 0
        for key in fields:
            newItem = QTableWidgetItem(key.decode())
            self.tableWidget_values.setItem(r, 0, newItem)
            value = self.values[key].decode()
            if len(self.values[key].decode()) > 1000:
                value = "....."
            newItem = QTableWidgetItem(value)
            self.tableWidget_values.setItem(r, 1, newItem)
            r += 1

    def getTableValue(self, row):
        # return self.tableWidget_values.item(row, 1).text()  # ##
        field = self.tableWidget_values.item(row, 0).text().encode()
        return self.values[field].decode()

    def displayField(self, row):
        self.field = self.getTableField(row)  # 需要保持，方便后面判断
        self.textEdit_key.setText(self.field)
        self.label_feild.setText(self.label_keyName)
        self.label_fieldSize.setText(str(len(self.field)))

        self.textEdit_key.setEnabled(True)

    def getTableField(self, row):
        return self.tableWidget_values.item(row, 0).text()

    def updateValue(self):
        # key_ = self.lineEdit_keyTitle.text()
        new_value = self.textEdit_value.toPlainText()
        new_field = self.textEdit_key.toPlainText()
        if new_field != self.field:
            self.opera.delRow(self.key_name, self.field)

        ret = self.opera.addData(self.key_name, new_field, new_value)

        if ret ==1:
            self.tableWidget_values.item(self.currentRow, 0).setText(new_field)
            self.tableWidget_values.item(self.currentRow, 1).setText(new_value)

    def addRowData(self, data):
        if self.type_ == data.get('type', None):
            field =  data.get('field', None)
            value = data.get('value', None)
            self.opera.addData(self.key_name, field, value)
            self.reloadValue()
    # def deleteRow(self):
    #     try:
    #         row = self.tableWidget_values.currentRow()
    #     except:
    #         return
    #     field = self.tableWidget_values.item(row, 0).text()
    #
    #     self.opera.delRow(self.key_name,field)