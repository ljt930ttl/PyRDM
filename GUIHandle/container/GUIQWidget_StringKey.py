#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQWidget_StringKey.py
@time: 2020/4/6 11:25
'''
# from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from GUIHandle.container.GUIQWidget_container_base import KeyContainerBase


class StringKeyContainer(KeyContainerBase):
    def __init__(self, key_name, values, TTL,opera):
        super().__init__(key_name, values, TTL,opera)
        self.type_ = 'string'

        self.initData()

    def initData(self):
        self.setTitle(self.type_, self.key_name, self.values)
        self.initDisplayArea()
        self.tableWidget_values.doubleClicked.connect(self.displayValue)


    def initDisplayArea(self):
        # title
        self.label_fieldCount.hide()
        self.widget_table_operation.hide()

        self.widget_View_Field.hide()
        self.horizontalLayout_title.addWidget(self.pushButton_reload_value)

        self.displayValue()

    def displayValue(self):
        self.textEdit_value.setText(self.values.decode())
        self.label_valueSize.setText(str(len(self.values)))

    def updateValue(self):
        value = self.textEdit_value.toPlainText()
        self.opera.setData(self.key_name, value)