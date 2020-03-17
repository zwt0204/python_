# -*- encoding: utf-8 -*-
"""
@File    : op.py
@Time    : 2020/3/16 10:39
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import numpy as np

# a = np.array([20, 30, 40, 50])
# b = np.arange(4)
# print(b)
# print(a - b)
# print(b**2)
# print(10*np.sin(a))
# print(a < 35)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
# 按照元素相乘
# print(A * B)
# 矩阵乘法
# print(A.dot(B))

a = np.ones((2, 3), dtype=int)
b = np.random.random((2, 3))
# print(a)
# print(b)
a *= 3
b += a
# print(a)
# print(b)
c = a + b
# print(c.dtype.name)
# print(np.exp(c*1j))
#
# print(c.sum())
# print(c.max())
# print(c.min())

d = np.arange(12).reshape(3, 4)
# print(d)
# print(d.sum(axis=0))
# print(d.min(axis=1))
# 每一行的累积总和
# print(d.cumsum(axis=1))

e = np.arange(3)
# print(e)
# print(np.exp(e))
# print(np.sin(e))
# print(np.sqrt(e))

f = np.arange(10) ** 3
# print(f)

# print(f[2:5])
# f[:6:2] = -1000
# print(f)
# print(f[:: -1])

i = np.arange(20).reshape(5, 4)

# print(i)

# print(i[2, 3])
#
# print(i[0:5, 1])
#
# print(i[:, 1])
# print(i[1:3, :])

# print(i[-1])

j = np.array([[[0, 1, 2],
               [10, 12, 13]],
              [[100, 101, 102],
               [110, 112, 113]]])
# print(j.shape)
# print(j[1, ...])

# 以最里面的为基准
# for row in i:
#     print(row, '=')

# for element in j.flat:
#     print(element)

