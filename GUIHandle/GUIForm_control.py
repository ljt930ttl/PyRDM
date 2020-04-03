#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/2 14:16
@Author:  linjinting
@File: GUIForm_control.py
@Software: PyCharm
"""
from PyQt5.QtWidgets import QWidget
from UI.ui_tabWidget_control import Ui_Qwidget_control

class FormControl(QWidget, Ui_Qwidget_control):
    def __init__(self):
        super(FormControl,self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    form = FormControl()
    form.show()
    sys.exit(app.exec_())