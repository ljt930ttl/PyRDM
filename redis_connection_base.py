#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2019/7/27 16:16
# @Author  : linjinting
# @Site    :
# @Software: redis_sync
# @File    : redis_connection_base.py
# @Function:

import redis

class RedisConnectionBase(object):
    __pool__ = None
    def __init__(self,arg):
        self.arg = arg
        pool = RedisConnectionBase.get_pool(arg)
        print(pool)
        self.redis_conn = redis.StrictRedis(connection_pool=pool,socket_timeout=500)


    @staticmethod
    def get_pool(arg):
        __pool  = None
        if RedisConnectionBase.__pool__ is None:
            RedisConnectionBase.__pool__ = redis.ConnectionPool(**arg, max_connections=10)

        return RedisConnectionBase.__pool__
    def __check_conn(self):
        """
        check the redis connction
        :return: True or False
        """
        try:
            self.redis_conn.ping()
            _msg = "[INFO]Connecting to redis was successful %s:%s\n" % (
                self.arg['host'], self.arg['port'])
            self.show_msg(_msg)
            return True
        except Exception as e:
            _msg = "%s\n" % (e)
            self.show_msg(_msg)
            return False

    def get_conn(self):
        """
        # Get the redis object
        :param rarg_d: redis arg
        :param connection_pool: redis connection_pool
        :return: m_rconn or None
        """
        if self.__check_conn():
            return self.redis_conn
        else:
            return None

    def show_msg(self, msg):
        """
        # show msg
        :param msg:
        :return:
        """
        print(msg)


if __name__ == '__main__':
    rarg_d = {
        "host": "127.0.0.1",
        "port": 6379
    }

    RC = RedisConnectionBase(rarg_d)
    redis_conn = RC.get_conn()
    # RC.get_conn(rarg_d)
