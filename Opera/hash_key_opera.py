#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 14:05
@Author:  linjinting
@File: hash_key_opera.py
@Software: PyCharm
"""
from Opera.abstract_opera import AbstractOpera


class HashOpera(AbstractOpera):
    def __init__(self, opera_type=None):
        super().__init__(opera_type)
        self.connection = None

    def getData(self, key, curs=0, count=1000):
        values_d = dict()

        while True:
            curs, values_ = self.connection.hscan(key, cursor=curs, count=count)
            values_d.update(values_)
            if curs == 0:
                break

        return values_d

    def setData(self, key, mapping):

        return self.connection.hmset(key, mapping)

    def addData(self, key, field, value):
        return self.connection.hset(key, field, value)

    def delRow(self, key, field):
        return self.connection.hdel(key, field)


    ### return list other getData
    def hgetall(self, key):
        return self.connection.hgetall(key)
