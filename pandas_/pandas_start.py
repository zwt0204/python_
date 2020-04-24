# -*- encoding: utf-8 -*-
"""
@File    : pandas_start.py
@Time    : 2020/3/17 15:36
@Author  : zwt
@git   : 
@Software: PyCharm
"""
"""
主要的数据结构:
Serices:一维数据
DataFrame:二维数据
"""
import numpy as np
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

dates = pd.date_range('20200318', periods=6)
# print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
# print(df2.dtypes)

# 从头数据
# print(df.head())
# 从尾取数据
# print(df.tail(3))

# 查看索引
# print(df.index)

# 查看列名
# print(df.columns)

# DataFrame.to_numpy() 的输出不包含行索引和列标签
# print(df.to_numpy())
# 数据的统计摘要
# print(df.describe())
# 转置
# print(df.T)
# 按照轴排序
# print(df.sort_index(axis=1, ascending=False))
# 按值排序
# print(df.sort_values(by='B'))

# print(df['A'])

# 切片
# print(df[0:3])
# 用标签提取一行数据
# print(df.loc[dates[0]])

# 用标签提取多列数据
# print(df.loc[:, ['A', 'B']])

print(df2)
# print(df.iloc[3])

# print(df.iloc[3:5, 0:2])
# 快速访问
# print(df.iat[1, 1])

# print(df.A > 0)
# print(df[df.A > 0])

# print(df[df > 0])

df2 = df2.copy()
df2['G'] = ['one', 'two', 'three', 'four']
# print(df2)

# 按标签赋值
df.at[dates[0], 'A'] = 0
# 按位置赋值
df.iat[0, 1] = 0
# print(df)

df.loc[:, 'D'] = np.array([5] * len(df))
# print(df)

# 缺失值为NaN

# 重建索引（reindex）可以更改、添加、删除指定轴的索引，并返回数据副本，即不更改原数据
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# print(df1)

a = df1.fillna(value=5)
# print(a)

# 删除所有含缺失值的行
b = df1.dropna(how='any')
# print(b)
# 统计
df.mean()

g = ['1', '2']
print(g.pop('1'))
