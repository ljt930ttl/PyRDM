#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 13:59
@Author:  linjinting
@File: abstract_opera.py
@Software: PyCharm
"""


class AbstractOpera(object):
    def __init__(self, opera_type=None):
        self.connection = None
        self.opera_type = opera_type

    def setConn(self, conn):
        self.connection = conn

    def save(self):
        return self.connection.save()

    def getKeyTTL(self, key):
        pass

    def getType(self, key=None):
        if self.opera_type is None and key is not None:
            self.opera_type = self.connection.type(key)
        return self.opera_type

    def scan(self, curs=0, count=10000):
        """
        :param curs:
        :param count:
        :return: keys (redis keys)
        """
        keys = list()
        # curs = 0
        while True:
            curs, values = self.connection.scan(cursor=curs, count=count)
            keys = keys + values
            if curs == 0:
                break
        return keys

    def getData(self, *args, **kwargs):
        pass

    def setData(self, *args, **kwargs):
        pass

    def delData(self, *names):
        self.connection.delete(*names)

    def addData(self, *args):
        pass

    def delRow(self, *args):
        pass

    def updateValue(self, *args):
        pass

