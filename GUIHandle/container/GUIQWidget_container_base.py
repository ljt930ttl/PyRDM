#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: GUIQWidget_container_base.py
@time: 2020/4/6 11:09
'''
from PyQt5.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from UI.ui_QWdiget_key_container import Ui_QWidget_key_container
from GUIHandle.container.GUIQdialog_add_value import AddValue
from GUIHandle.container.GUIQdialog_set_ttl import SetTTLDialog
from GUIHandle.communicate import bus
from utils.chars_proc import CodingChar

class KeyContainerBase(QWidget, Ui_QWidget_key_container):
    def __init__(self, key_name, values, TTL, opera):
        super(KeyContainerBase, self).__init__()
        self.setupUi(self)
        self.codingChar = CodingChar

        self.key_name = key_name
        self.values = values
        self.TTL = TTL
        self.opera = opera
        self.value = None
        self.valueTypes = []
        self.currentRow = 0

        self.initSingle()

    def initSingle(self):
        self.tableWidget_values.doubleClicked.connect(self.displayValue)
        self.pushButton_setTTL.clicked.connect(self.setTTLDialog)

        self.pushButton_addRow.clicked.connect(self.addRowDialog)
        self.pushButton_deleteRow.clicked.connect(self.deleteRow)
        self.pushButton_reload_value.clicked.connect(self.reloadValue)
        self.pushButton_save.clicked.connect(self.updateValue)

        bus.addRowData.connect(self.addRowData)
        bus.setTTLValue.connect(self.setTTL)

    def initData(self):
        """
        hash ,zset , string单独重构,  list,set 共用基类
        :return:
        """
        self.setTitle(self.type_, self.key_name, self.values)
        self.initDisplayArea()

    def setTitle(self, type_, key_name, values):
        type_ = type_.upper() + ":"
        self.label_keyType.setText(type_)
        self.lineEdit_keyTitle.setText(key_name)
        values_count = 'Size: %d' % (len(values))
        self.label_fieldCount.setText(values_count)

        ttl_count = 'TTL: %d' % (self.TTL)
        self.label_TTL.setText(ttl_count)

    def initDisplayArea(self):
        """
        hash ,zset , string单独重构,  list,set 共用基类
        :return:
        """
        self.createTable(self.values)
        self.widget_View_Field.hide()
        self.textEdit_value.setEnabled(False)

    def createTable(self, fields):
        """
        hash ,zset , 单独重构, string忽略,  list,set 共用基类
        :return:
        """
        self.tableWidget_values.setColumnCount(1)
        self.tableWidget_values.setRowCount(len(fields))
        self.tableWidget_values.setHorizontalHeaderLabels(self.tableHeaders)
        self.tableWidget_values.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget_values.setSelectionBehavior(QTableWidget.SelectRows)  # 整行选中的方式
        self.tableWidget_values.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget_keys.resizeColumnsToContents()  # 将列调整到跟内容大小相匹配
        # self.tableWidget_keys.resizeRowsToContents()  # 将行大小调整到跟内容的大学相匹配
        r = 0
        for value in fields:
            # new_value, type_ = self.codingChar.codingString(value)
            # self.valueTypes.append(type_)
            newItem = QTableWidgetItem(value.decode('utf-8', errors='replace'))
            self.tableWidget_values.setItem(r, 0, newItem)
            r += 1

    def displayValue(self):
        """
        hash ,zset , string单独重构, list,set 共用基类
        :return:
        """
        self.currentRow = self.tableWidget_values.currentRow()
        self.value = self.getTableValue(self.currentRow)  # ##
        self.textEdit_value.setText(self.value)
        self.label_valueSize.setText(str(len(self.value)))

        self.textEdit_value.setEnabled(True)
        self.displayField(self.currentRow)

    def getTableValue(self, row):
        return self.tableWidget_values.item(row, 0).text()  # ##

    def displayField(self, row):
        pass

    def updateValue(self):
        pass

    def setTTL(self, ttl):
        self.opera.setTTL(self.key_name, ttl)
        self.label_TTL.setText(str(ttl))

    def setTTLDialog(self):
        ttl_dialog = SetTTLDialog(self.TTL)
        ttl_dialog.exec_()
        ttl_dialog.destroy()

    def deleteRow(self):
        """
        string 没有该函数调用
        :return:
        """
        try:
            row = self.tableWidget_values.currentRow()
        except:
            return

        value = self.tableWidget_values.item(row, 0).text()
        self.opera.delRow(self.key_name, value)
        self.reloadValue()

    def addRowData(self, *args):
        """
        hash,zset,set,list 都单独重构，string忽略
        :return:
        """
        pass

    def addRowDialog(self):
        """
        string 没有该函数调用
        :return:
        """
        dialog_add = AddValue(self.type_)

        dialog_add.exec_()
        # rInfo = dialog_conn.sendredisConnInfo()
        dialog_add.destroy()

    def reloadValue(self):
        bus.containerReload.emit()
        self.close()


