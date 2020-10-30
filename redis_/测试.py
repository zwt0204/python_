#!/user/bin/env python
# coding=utf-8
"""
@file: 测试.py
@author: zwt
@time: 2020/10/30 16:06
@desc: 
"""
import redis
from redis_.cache.data_object import DataObject


def get_session(session_id):
    """获取信息"""
    sess = DataObject(session_id)
    return sess


def add_data(sess, data):
    sess.data = data


sess = get_session('')
add_data(sess, '你好')
sess.save()




# r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='')
# print(r)
# # r.set("dir:dir:dir:key", "value")
#
# res = r.get("dir:dir:dir:key")
# print(str(res, encoding="utf8"))