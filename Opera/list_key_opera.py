#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 14:05
@Author:  linjinting
@File: hash_key_opera.py
@Software: PyCharm
"""
from Opera.abstract_opera import AbstractOpera


class ListOpera(AbstractOpera):
    def __init__(self, opera_type=None):
        super().__init__(opera_type)
        self.connection = None

    def getData(self, key, start=0, end=-1, limit=10000):
        # lrange
        value_l = list()
        start = start
        residue = self.connection.llen(key)  # 剩余数
        while True:
            if residue > limit:
                end = start + limit
            else:
                end += residue
            value_l.extend(self.connection.lrange(key, start, end))
            start = end
            residue -= limit
            if residue < 0:
                break
        return value_l

    def setData(self, key, *value):
        return self.connection.rpush(key, *value)

    def addData(self, key,row, value):
        return self.connection.lset(key, row, value)

    def delRow(self, key, value):
        # 删除单个值
        # RDM 先 lrnger 在lset，还没研究为什么
        self.connection.lrem(key, 1, value)

    def delRows(self, key, value, count):
        self.connection.lren(key, count, value)
