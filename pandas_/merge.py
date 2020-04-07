# -*- encoding: utf-8 -*-
"""
@File    : merge.py
@Time    : 2020/3/19 11:31
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(10, 4))
# print(df)

pieces = [df[: 3], df[3: 7], df[7:]]
# print(pieces)

c = pd.concat(pieces)
# print(c)
