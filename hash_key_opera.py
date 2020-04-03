#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 14:05
@Author:  linjinting
@File: hash_key_opera.py
@Software: PyCharm
"""
from abstract_key_opera import AbstractKeyOpera


class HashKeyOpera(AbstractKeyOpera):
    def __init__(self):
        super().__init__()
        self.connection = None

    def getData(self, key, curs=0, count=1000):
        values_d = dict()
        if self.connection is None:
            return None
        while True:
            curs, values_ = self.connection.hscan(key, cursor=curs, count=count)
            values_d.update(values_)
            if curs == 0:
                break

        return values_d

    # def addData(self):
    #     pass

    def delData(self,key, field):

        self.connection.hdel(key, field)

    def update(self,key ,field, value):
        if self.connection is None:
            return None

        self.connection.hset(key, field, value)

    def setConn(self,conn):
        self.connection = conn
