# -*- encoding: utf-8 -*-
"""
@File    : decorator.py
@Time    : 2020/4/23 10:31
@Author  : zwt
@git   : 
@Software: PyCharm
"""
from datetime import datetime
import time


class demo:

    def __init__(self):
        self.name = 'hah'
        self.value = '123'


def timer(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        end = datetime.now()
        print((end - start).seconds)

    return wrapper


@timer
def demo():
    time.sleep(3)


import hashlib
import pickle
import redis
from functools import wraps

r = redis.Redis(host="localhost", port=6379, db=7)


def _compute_key(function, args, kw):
    """序列化并求其哈希值"""
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()


def memorize(duration=-1):
    """自动缓存"""

    def _memoize(function):
        @wraps(function)  # 自动复制函数信息
        def __memoize(*args, **kw):
            key = _compute_key(function, args, kw)
            # 是否已缓存？
            if r.exists(key):
                try:  # 判断存在和返回之间还有一段时间，可能造成key不存在
                    return r[key]
                except:
                    pass
            # 运行函数
            result = function(*args, **kw)
            # 保存结果
            # r[key] = result
            r.set(name=key, value=result)
            r.expire(key, duration)
            return result

        return __memoize
    return _memoize


@memorize(3600)
def a_test_f():
    """一个需要缓存的函数"""
    print('get result')
    from time import sleep
    import random
    sleep(2)
    demo.value = random.randint(1, 100)
    return demo


if __name__ == '__main__':
    # demo()
    a_test_f()
