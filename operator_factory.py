#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
# Author:linjinting for 02010166
@file: operator_factory.py
@time: 2020/4/5 15:13
'''

from redis_connection_base import RedisConnectionBase

from Opera.hash_key_opera import HashOpera
from Opera.zset_key_opera import ZSetOpera
from Opera.set_key_opera import SetOpera
from Opera.list_key_opera import ListOpera
from Opera.string_key_opera import StringOpera
from Opera.abstract_opera import AbstractOpera


class OperatorFactory(object):
    mapOpera = {
        b'string': StringOpera,
        b'list': ListOpera,
        b'set': SetOpera,
        b'zset': ZSetOpera,
        b'hash': HashOpera,
        'redis': AbstractOpera

    }

    def __init__(self, conn=None):
        self.operator = None
        # self.opera_type = None
        if conn is None:
            arg = {"host": "127.0.0.1", "port": 6379}
            conn = RedisConnectionBase(arg)
        self.connection = conn

    def createOperator(self, opera_type=None, key=None):
        if opera_type is None and key is not None:
            opera_type = self.connection.type(key)
        Operator = self.mapOpera.get(opera_type, None)
        self.operator = Operator(opera_type)
        self.operator.setConn(self.connection)
        return self.operator


if __name__ == '__main__':
    td = {'a':'b'}
    s = td.get(None,None)
    print(s)