#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 11:00
@Author:  linjinting
@File: communicate.py
@Software: PyCharm
"""
from PyQt5.QtCore import pyqtSignal, QObject


class CommunicateBus(QObject):
    createServerItem = pyqtSignal(dict)
    clickedKeyItem = pyqtSignal(dict)


bus = CommunicateBus()