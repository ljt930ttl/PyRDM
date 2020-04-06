#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQWidget_SetKey.py
@time: 2020/4/6 10:58
'''

from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from GUIHandle.container.GUIQWidget_container_base import KeyContainerBase


class SetKeyContainer(KeyContainerBase):
    def __init__(self, key_name, values, type_):
        super().__init__(key_name, values, type_)
        self.setupUi(self)

        # self.key_name = key_name
        # self.values = values
        # self.type_ = type_
        self.tableHeaders = ['value']
        self.initData()

    def initData(self):
        # fields = self.values

        self.setTitle(self.type_, self.key_name, self.values)
        self.createTable(self.values)

        self.tableWidget_values.doubleClicked.connect(self.displayValue)

    def setTitle(self, type_, key_name, values):
        text_ = type_.upper() + ":"
        self.label_keyType.setText(text_)
        self.lineEdit_keyTitle.setText(key_name)
        values_count = 'Size: %d'%(len(values))
        self.label_fieldCount.setText(values_count)

        # ttl_count = 'TTL: %d' % (len(ttl))
        # self.label_TTL.setText(ttl_count)

    def displayField(self, row):
        self.widget_View_Field.hide()
        # self.label_fieldSize.setText(str(len(source)))

    def displayValue(self):
        row = self.tableWidget_values.currentRow()
        value = self.__getTableValue(row)  # ##
        self.textEdit_value.setText(value)
        self.label_valusSize.setText(str(len(value)))

        self.displayField(row)

    def __getTableValue(self, row):
        return self.tableWidget_values.item(row, 0).text()  # ##