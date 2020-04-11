#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/7 10:38
@Author:  linjinting
@File: GUITable_mixin.py
@Software: PyCharm
"""

class TableMixin(object):


    def displayValue(self):
        row = self.tableWidget_values.currentRow()
        value = self.getTableValue(row)  # ##
        self.textEdit_value.setText(value)
        self.label_valueSize.setText(str(len(value)))

        self.displayField(row)

    def getTableValue(self, row):
        return self.tableWidget_values.item(row, 0).text()  # ##