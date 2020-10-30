#!/user/bin/env python
# coding=utf-8
"""
@file: config.py
@author: zwt
@time: 2020/10/30 16:37
@desc: 
"""
EXPIRE_TIME = 10 * 60 * 60
IF_CACHE = True

REDIS_DB = {
    'host': '127.0.0.1',
    'port': '6379',
    'db': '0',
    'password': '',
    'max_connections': 10,
    'socket_connect_timeout': 0.5,
}