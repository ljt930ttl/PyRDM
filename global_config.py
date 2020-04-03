#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :   2020/4/2 15:10
@Author:  linjinting
@File: global_config.py
@Software: PyCharm
"""

rdm_config = dict()
mapServer = dict()
def redisConfig(name='127.0.0.1', host='127.0.0.1', port=6379,
             db=0, password=None, socket_timeout=None,
             socket_connect_timeout=None,
             socket_keepalive=None, socket_keepalive_options=None,
             connection_pool=None, unix_socket_path=None,
             encoding='utf-8', encoding_errors='strict',
             charset=None, errors=None,
             decode_responses=False, retry_on_timeout=False,
             ssl=False, ssl_keyfile=None, ssl_certfile=None,
             ssl_cert_reqs=None, ssl_ca_certs=None,
             max_connections=None, separator=":"):
    config = {
        'db': db,
        'password': password,
        'host': host,
        'port': port,
    }
    rdm_config.update({
        'config': config,
        'name': name,
        'separator': separator
    })


if __name__ == '__main__':
    s = b'aa'.decode()
    a = s.upper()
    print(a)
