# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/5/29 15:57
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import numpy as np
import faiss

d = 512  # 维数
n_data = 2000
np.random.seed(0)
data = []
mu = 3
sigma = 0.1
for i in range(n_data):
    data.append(np.random.normal(mu, sigma, d))
data = np.array(data).astype('float32')

query = []
n_query = 10
mu = 3
sigma = 0.1
np.random.seed(12)
for i in range(n_query):
    query.append(np.random.normal(mu, sigma, d))
query = np.array(query).astype('float32')

index = faiss.IndexFlatL2(d)  # 构建index
print(index.is_trained)  # False时需要train
index.add(data)  # 添加数据
print(index.ntotal)  # index中向量的个数
