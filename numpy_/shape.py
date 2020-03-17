# -*- encoding: utf-8 -*-
"""
@File    : shape.py
@Time    : 2020/3/16 11:28
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import numpy as np

# a = np.floor(10*np.random.random((3, 4)))
# print(a)
# print(a.shape)

# 返回更改后的数据，不更改原始数据
# print(a.reshape(6, 2))
# print(a.T)
# 直接修改原数据
# a.resize((6, 2))
# print(a)
# print(a.reshape(3, -1))

# a = np.floor(10 * np.random.random((2, 2)))
# b = np.floor(10 * np.random.random((2, 2)))
# print(np.vstack((a, b)))
# print(np.hstack((a, b)))

# c = np.floor(10 * np.random.random((2, 12)))
# print(c)
# print(np.hsplit(c, (3, 4)))

# 完全不复制
a = np.arange(12)
b = a

# a new array object with new data is created
d = a.copy()
