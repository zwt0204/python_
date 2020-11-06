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
import json


def get_session(session_id):
    """获取信息"""
    sess = DataObject(session_id)
    return sess


def add_data(sess, data):
    sess.data = data


sess = get_session('d324d23a1a9611eb8a7d70b5e8a3a45b')
print(sess)
# add_data(sess, '你好')
# sess.save()
print(str(sess.data, encoding='utf8'))
print(json.loads(str(sess.data, encoding='utf8')))



# r = redis.Redis(host='127.0.0.1', port=6379, db=0, password='')
# print(r)
# # r.set("dir:dir:dir:key", "value")
#
# res = r.get("dir:dir:dir:key")
# print(str(res, encoding="utf8"))