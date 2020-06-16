# -*- encoding: utf-8 -*-
"""
@File    : contextmanager.py
@Time    : 2020/6/8 15:47
@Author  : zwt
@git   : 
@Software: PyCharm
"""
from contextlib import contextmanager


"""
自定义实现with结构
"""


@contextmanager
def myOpen(name, state, **kwargs):
    f = open(name, state)
    yield f
    f.close()


if __name__ == '__main__':
    with myOpen('train.txt', 'r', encoding='utf8') as f:
        print(f.readlines())