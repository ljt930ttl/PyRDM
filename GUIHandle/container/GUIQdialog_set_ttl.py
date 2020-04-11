#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/9 9:41
@Author:  linjinting
@File: GUIQdialog_set_ttl.py
@Software: PyCharm
"""

from PyQt5.QtWidgets import QDialog
from UI.ui_Dialog_setTTL import Ui_Dialog_SetTTL
from GUIHandle.communicate import bus


class SetTTLDialog(QDialog, Ui_Dialog_SetTTL):
    def __init__(self,ttl):
        super().__init__()
        self.setupUi(self)

        self.ttl = ttl

        self.lineEdit_ttl.setText(str(ttl))

        self.pushButton_save.clicked.connect(self.save)
        self.pushButton_cancel.clicked.connect(self.close)

    def save(self):

        ttl = self.lineEdit_ttl.text()
        bus.setTTLValue.emit(int(ttl))
        self.close()

