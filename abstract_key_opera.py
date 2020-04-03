#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 13:59
@Author:  linjinting
@File: abstract_key_opera.py
@Software: PyCharm
"""


class AbstractKeyOpera(object):
    def __init__(self):
        pass

    def getKeyTTL(self, key):
        pass

    def getKeyType(self, key):
        pass

    def getData(self, *args, **kwargs):
        pass

    def addData(self, *args):
        pass

    def delData(self, *args):
        pass

    def update(self, *args):
        pass