#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQWidget_ListKey.py
@time: 2020/4/6 11:24
'''
# from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from GUIHandle.container.GUIQWidget_container_base import KeyContainerBase


class ListKeyContainer(KeyContainerBase):
    def __init__(self, key_name, values, TTL,opera):
        super().__init__(key_name, values, TTL,opera)

        self.type_ = 'list'
        self.tableHeaders = ['value']

        self.initData()

    def updateValue(self):
        _value = self.textEdit_value.toPlainText()
        # new_value = self.codingChar.recoverCodeing(_value, self.valueTypes[self.currentRow])
        self.opera.addData(self.key_name, self.currentRow, _value)

        self.tableWidget_values.item(self.currentRow, 0).setText(_value)

    def addRowData(self, data):
        if self.type_ == data.get('type', None):

            new_value = data.get('value', None)
            # new_value = self.codingChar.recoverCodeing(data.get('value', None), self.valueTypes[self.currentRow])

            self.opera.setData(self.key_name, new_value)
            self.reloadValue()