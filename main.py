#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/2 16:20
@Author:  linjinting
@File: main.py
@Software: PyCharm
"""
import sys
from PyQt5.QtWidgets import QApplication
from GUIHandle.GUIMainWindowRDM import MainWindowRDM

def main():
    app = QApplication(sys.argv)
    window = MainWindowRDM()
    window.show()
    sys.exit(app.exec_())


main()
