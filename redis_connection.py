#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/3 13:41
@Author:  linjinting
@File: redis_connection.py
@Software: PyCharm
"""
from redis_connection_base import RedisConnectionBase
from hash_key_opera import  HashKeyOpera

class RedisConneciton(object):
    def __init__(self, arg=None):
        if arg is None:
            arg = {"host": "127.0.0.1", "port": 6379}
        RC = RedisConnectionBase(arg)
        self.connection = RC.get_conn()
        self.opera_ship = {
            b'string': "",
            b'list': "",
            b'set': "",
            b'zset': "",
            b'hash': HashKeyOpera(),
        }

    def getData(self,key_name):
        type_ = self.connection.type(key_name)

        opera = self.opera_ship.get(type_, None)
        if opera is  None:
            return
        opera.setConn(self.connection)
        return (type_, opera.getData(key_name),opera)



    def scan(self, curs=0, count=10000):
        """

        :param _rconn: redis conn object
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