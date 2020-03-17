# -*- encoding: utf-8 -*-
"""
@File    : start_numpy.py
@Time    : 2020/3/16 9:47
@Author  : zwt
@git   : 
@Software: PyCharm
"""
"""
numpy数组在创建时具有固定的大小，python的原生数组对象可以动态增长
np.ndim-数组的维度的个数，
np.shape-数组的维度
np.size-数组元素的总数
np.dtype-数组元素类型的对象
np.itemsize-数组中每个元素的字节大小
np.data-该缓冲区包含数组的实际元素
"""
import numpy as np

a = np.arange(15).reshape(3, 5)
# print(a)
# print(a.shape)
# print(a.ndim)
# print(a.dtype.name)
# print(a.itemsize)
# print(type(a))
b = np.array([6, 7, 8])
# print(b)
# print(type(b))

c = np.array([2, 3, 4])
# print(c)

# b = np.array([1.2, 3.5, 5.1])
# print(b)
# print(b.itemsize)

d = np.array([(1.5, 2.3), (4.5, 6)])
# print(d)
e = np.array([[1, 2], [3, 4]], dtype=complex)
# print(e)

f = np.zeros((3, 4))
# print(f)

g = np.ones((2, 3, 4), dtype=np.int16)
# print(g)

# 随机内容
h = np.empty((2, 3))
# print(h)

i = np.arange(10, 30, 5)
# print(i)

j = np.arange(0, 3, 0.3)
# print(j)

from numpy import pi

k = np.linspace(0, 2, 9)
# print(k)

# print(pi)
x = np.linspace(0, 2*pi, 100)
# print(x)
l = np.sin(x)
# print(l)

m = np.arange(24).reshape(2, 3, 4)
print(type(m))
