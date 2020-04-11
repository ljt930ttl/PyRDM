#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQwidget_ZSetKey.py
@time: 2020/4/6 10:56
'''
from PyQt5.QtWidgets import QTableWidgetItem,QTableWidget,QLineEdit
from GUIHandle.container.GUIQWidget_container_base import KeyContainerBase


class ZSetKeyContainer(KeyContainerBase):
    def __init__(self, key_name, values, TTL, opera):
        super().__init__(key_name, values, TTL, opera)

        # self.key_name = key_name
        # self.values = values
        self.type_ = 'zset'

        self.tableHeaders = ['value', 'source']
        self.label_keyName = 'Source:'
        self.initData()

    def initData(self):
        # fields = self.values

        self.setTitle(self.type_, self.key_name, self.values)
        self.initDisplayArea()

        self.tableWidget_values.doubleClicked.connect(self.displayValue)
        # self.displayValue()

    def initDisplayArea(self):
        self.createTable(self.values)
        self.textEdit_key.setEnabled(False)
        self.textEdit_value.setEnabled(False)

        self.lineEdit_key = QLineEdit()
        self.lineEdit_key.setEnabled(False)
        self.verticalLayout_field.addWidget(self.lineEdit_key)
        self.textEdit_key.hide()

    def createTable(self, fields):
        self.tableWidget_values.setColumnCount(2)
        self.tableWidget_values.setRowCount(len(fields))
        self.tableWidget_values.setHorizontalHeaderLabels(self.tableHeaders)
        self.tableWidget_values.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_values.setSelectionBehavior(QTableWidget.SelectRows)  # 整行选中的方式
        self.tableWidget_values.horizontalHeader().setStretchLastSection(True)

        r = 0
        for value, source in fields:
            newItem = QTableWidgetItem(value.decode())
            self.tableWidget_values.setItem(r, 0, newItem)
            newItem = QTableWidgetItem(str(source))
            self.tableWidget_values.setItem(r, 1, newItem)
            r += 1

    def getTableValue(self, row):
        return self.tableWidget_values.item(row, 0).text()  # ##

    def displayField(self, row):
        source = self.getTableField(row)

        # self.lineEdit_key = QLineEdit(self.widget_View_Field)
        self.lineEdit_key.setText(source)
        self.label_feild.setText(self.label_keyName)
        self.lineEdit_key.setEnabled(True)

    def getTableField(self, row):
        return self.tableWidget_values.item(row, 1).text()

    #  ##
    def updateValue(self):
        new_value = self.textEdit_value.toPlainText()
        new_field = self.lineEdit_key.text()
        try:
            source = float(new_field)
        except:
            print('error')
            return
        # if new_field != self.field:
        #     self.opera.delData(self.key_name, self.field)
        ret = self.opera.delRow(self.key_name, self.value)
        print(ret)
        ret = self.opera.addData(self.key_name, source, new_value)

        print(ret)

        self.tableWidget_values.item(self.currentRow, 0).setText(new_value)
        self.tableWidget_values.item(self.currentRow, 1).setText(new_field)

    def addRowData(self, data):
        if self.type_ == data.get('type', None):
            source =  data.get('field', None)
            new_value = data.get('value', None)
            self.opera.addData(self.key_name, source, new_value)
            self.reloadValue()