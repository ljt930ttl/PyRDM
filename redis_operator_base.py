#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2019/7/27 16:44
# @Author  : linjinting
# @Site    : 
# @Software: redis_sync
# @File    : redis_operator_base.py
# @Function:

class RedisOperatorBase(object):
    def __init__(self):
        self.connection = None
        pass

    # def ping(self):
    #     self.connection.ping()

    def setConn(self, conn):
        self.connection = conn

    # def type(self, key):
    #     return self.connection.type(key)

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




    def hscan(self, key, curs=0, count=None):
        fieldvalue_d = dict()

        while True:
            curs, _fieldvalue_d = self.connection.hscan(key, cursor=curs, count=count)
            fieldvalue_d.update(_fieldvalue_d)
            if curs == 0:
                break

        return fieldvalue_d

    def sscan(self, key, curs=0, count=None):
        value_l = list()

        while True:
            curs, _value = self.connection.sscan(key, cursor=curs, count=count)
            value_l = value_l + _value
            if curs == 0:
                break

        return value_l

    def zscan(self, key, curs=0, count=None):

        fieldvalue_d = dict()
        while True:
            curs, _fieldvalue_d = self.connection.zscan(key, cursor=curs, count=count)
            fieldvalue_d.update(_fieldvalue_d)
            if curs == 0:
                break
        return fieldvalue_d

    ## string read all
    def get(self, key):
        return self.connection.get(key)

    def set(self, key, value):
        return self.connection.set(key, value)

    ## list read all
    def rpush(self, key, *value):
        return self.connection.rpush(key, *value)

    def lrange(self, key, start, end, limit=1000):
        value_l = list()
        start = start

        residue = self.connection.llen(key) - 1  ###剩余数

        while True:
            if residue > limit:
                end = start + limit
            else:
                end = end

            _value = self.connection.lrange(key, start, end)
            value_l = value_l + _value

            start = end + 1
            residue -= limit + 1
            # print("residue", residue)
            if residue < 0:
                break

        return value_l

    ## set
    def smembers(self, key):
        return self.connection.smembers(key)

    def sadd(self, key, *value):
        return self.connection.sadd(key, *value)

    ## zset read all
    def zrange(self, key, start=0, end=-1, desc=False, withscores=False, limit=10000):
        """
        :param _rconn:
        :param key:
        :param limit:
        :param desc:
        :param withscores:
        :param :score_cast_func
        :return:
        """
        value_l = list()
        start = start
        num = self.connection.zcard(key) - 1  ###999

        while True:
            if num > limit:
                end = start + limit
            else:
                end = end

            _value = self.connection.zrange(key, start, end, desc=desc, withscores=withscores, )
            value_l = value_l + _value

            start = end + 1
            num -= limit + 1
            if num < 0:
                break

        return value_l

    def zadd(self, key, mapping):
        return self.connection.zadd(key, mapping)

    ## hash read all
    def hgetall(self, key):
        # print(self._rconn)
        return self.connection.hgetall(key)
    #  hash write
    def hmset(self, key, mapping):
        try:
            rs = self.connection.hmset(key, mapping)
        except:
            print(key, mapping)
            raise
        return rs

    def hset(self, key, field, value):
        return self.connection.hset(key, field, value)

    def save(self):
        return self.connection.save()

if __name__ == '__main__':

    rarg_d = {
        "host": "127.0.0.1",
        "port": 6379
    }

