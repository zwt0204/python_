# -*- encoding: utf-8 -*-
"""
@File    : basic_np.py
@Time    : 2020/3/17 10:07
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import numpy as np

a = np.arange(3, dtype=np.float)
print(a.dtype.name)
# 转换数据类型
print(a.astype(int).dtype.name)

print(np.issubdtype(a.dtype, np.integer))
# 每个维度表示该维度中的变化
b = np.indices((3, 3))
# print(b)

y = np.arange(35).reshape(5, 7)
# print(y)
# print(y[1:5:2, ::3])

# print(y[np.array([0, 2, 4])])

x = np.arange(30).reshape((2, 3, 5))
# print(x)
n = np.array([[True, True, False], [False, True, True]])
# print(x[n])


print(y.shape)
print(y[:, np.newaxis, :].shape)
# print(y[:, np.newaxis, :])

