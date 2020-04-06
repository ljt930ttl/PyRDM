#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 14:05
@Author:  linjinting
@File: hash_key_opera.py
@Software: PyCharm
"""
from Opera.abstract_opera import AbstractOpera


class StringOpera(AbstractOpera):
    def __init__(self, opera_type=None):
        super().__init__(opera_type)
        self.connection = None

    def getData(self, key):
        values = self.connection.get(key)

        return values

    def setData(self, key, value):
        if self.connection is None:
            return None

        self.connection.set(key, value)



