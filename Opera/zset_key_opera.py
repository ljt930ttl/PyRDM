#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 14:05
@Author:  linjinting
@File: hash_key_opera.py
@Software: PyCharm
"""
from Opera.abstract_opera import AbstractOpera


class ZSetOpera(AbstractOpera):
    def __init__(self, opera_type=None):
        super().__init__(opera_type)
        self.connection = None

    def getData(self, key, curs=0, count=None):
        """

        :param key:
        :param curs:
        :param count:
        :return: dict: {member:score...}
        """
        value_l = list()
        while True:
            curs, value = self.connection.zscan(key, cursor=curs, count=count)
            value_l.extend(value)
            if curs == 0:
                break
        return value_l

    def setData(self, key, mapping):

        return self.connection.zadd(key, mapping)

    def addData(self, key, mapping):
        return self.connection.zadd(key, mapping)

    def delRow(self, key, field):
        return self.connection.zrem(key, field)

    def updateValue(self, key, mapping):
        self.delRow(key, mapping.values()[0])
        return self.addData(key, mapping)

    ### other
    def zrange(self, key, start=0, end=-1, withscores=True, desc=False, limit=10000):
        value_l = list()
        residue = self.connection.zcard(key) - 1  ###999

        while True:
            if residue > limit:
                end = start + limit - 1
            else:
                end += residue
            value_l.extend(self.connection.zrange(key, start, end, desc=desc, withscores=withscores)) #[member,source...]
            start = end
            residue -= limit
            if residue < 0:
                break
        return value_l
