#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQWidget_SetKey.py
@time: 2020/4/6 10:58
'''

# from PyQt5.QtWidgets import QTableWidgetItem
from GUIHandle.container.GUIQWidget_container_base import KeyContainerBase

class SetKeyContainer(KeyContainerBase):
    def __init__(self, key_name, values, TTL,opera):
        super().__init__(key_name, values, TTL,opera)

        # self.key_name = key_name
        # self.values = values
        self.type_ = 'set'
        self.tableHeaders = ['value']
        self.initData()

    def updateValue(self):
        new_value = self.textEdit_value.toPlainText()

        self.opera.delRow(self.key_name, new_value)
        self.opera.addData(self.key_name, new_value)
        self.tableWidget_values.item(self.currentRow, 0).setText(new_value)

    def addRowData(self, data):
        if self.type_ == data.get('type', None):
            new_value = data.get('value', None)
            self.opera.addData(self.key_name, new_value)
            self.reloadValue()