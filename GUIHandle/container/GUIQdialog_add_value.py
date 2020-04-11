#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/8 19:45
@Author:  linjinting
@File: GUIQdialog_add_value.py
@Software: PyCharm
"""
from PyQt5.QtWidgets import QDialog, QLineEdit, QPushButton
from UI.ui_QWdiget_key_container import Ui_QWidget_key_container
from GUIHandle.communicate import bus


class AddValue(QDialog, Ui_QWidget_key_container):
    def __init__(self, type_):
        super().__init__()
        self.setupUi(self)
        self.type_ = type_
        self.initArea()
        self.initSingel()
        self.setWindowTitle('Add Row')

    def initSingel(self):
        self.pushButton_save.clicked.connect(self.saveData)
        self.pushButton_cancel.clicked.connect(self.cancel)

    def initArea(self):
        self.widget_table_operation.hide()
        self.widget_title.hide()

        self.pushButton_cancel = QPushButton(self.widget_value)
        self.pushButton_cancel.setText('cancel')
        self.horizontalLayout_save.removeWidget(self.pushButton_save)
        self.horizontalLayout_save.addWidget(self.pushButton_cancel)
        self.horizontalLayout_save.addWidget(self.pushButton_save)

        if self.type_ == 'zset':
            self.lineEdit_key = QLineEdit()
            self.verticalLayout_field.addWidget(self.lineEdit_key)
            self.textEdit_key.hide()
            self.label_feild.setText('Source:')

        if self.type_ == 'set' or self.type_ == 'list':
            self.widget_View_Field.hide()

    def saveData(self):
        if self.type_ == 'zset':
            value = self.textEdit_value.toPlainText()
            source = self.lineEdit_key.text()
            try:
                source = float(source)
            except:
                print('error')
                return
            data = {'type': self.type_, 'value': value, 'field': source}
        elif self.type_ == 'set' or self.type_ == 'list':
            value = self.textEdit_value.toPlainText()
            data = {'type': self.type_, 'value': value}
        elif self.type_ == 'hash':
            value = self.textEdit_value.toPlainText()
            field = self.textEdit_key.toPlainText()
            data = {'type': self.type_, 'value': value, 'field': field}
        else:
            print('error')
            return
        bus.addRowData.emit(data)
        self.close()

    def cancel(self):
        self.close()
