#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 14:05
@Author:  linjinting
@File: hash_key_opera.py
@Software: PyCharm
"""
from Opera.abstract_opera import AbstractOpera


class SetOpera(AbstractOpera):
    def __init__(self, opera_type=None):
        super().__init__(opera_type)
        self.connection = None

    def getData(self, key, curs=0, count=10000):
        # sscan
        value_l = list()
        while True:
            curs, _value = self.connection.sscan(key, cursor=curs, count=count)
            value_l.extend(_value)
            if curs == 0:
                break

        return value_l

    def setData(self, key, *value):
        if self.connection is None:
            return None
        return self.connection.sadd(key, *value)

    def addData(self, key, *value):
        if self.connection is None:
            return None
        return self.connection.sadd(key, *value)

    def delRow(self, key, value):
        return self.connection.srem(key, value)


    def updateValue(self, key, value):
        # set 先删除后添加，即是修改
        if self.connection is None:
            return None
        self.delRow(key, value)
        return self.addData(key, value)


    # other
    def smembers(self, key):
        return self.connection.smembers(key)