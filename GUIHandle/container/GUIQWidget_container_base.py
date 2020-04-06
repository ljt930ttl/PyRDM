#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQWidget_container_base.py
@time: 2020/4/6 11:09
'''
from PyQt5.QtWidgets import QWidget
from UI.ui_QWdiget_key_container import Ui_QWidget_key_container


class KeyContainerBase(QWidget, Ui_QWidget_key_container):
    def __init__(self, key_name, values, type_):
        super(KeyContainerBase, self).__init__()
        self.setupUi(self)

        self.key_name = key_name
        self.values = values
        self.type_ = type_
        self.initData()

    def initData(self):
        pass

    def setTitle(self, type_, key_name, fields):
        pass

    def createTable(self, fields):
        pass

    def setTableData(self, fields):
        pass

    def displayField(self, row):
        pass

    def displayValue(self):
        pass

    def __getTableValue(self, row):
        pass

    def __getTableField(self, row):
        pass

    def updateValue(self):
        pass