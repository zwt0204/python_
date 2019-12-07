# -*- encoding: utf-8 -*-
"""
@File    : Counting_Sort.py
@Time    : 2019/12/7 13:38
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Count:

    def __init__(self):
        super(Count, self).__init__()

    def run(self, data):
        length = len(data)
        res = [0] * length
        for i in range(length):
            p = 0
            for j in range(length):
                if data[i] > data[j]:
                    p += 1
            res[p] = data[i]
        return res


model = Count()
a = model.run([3, 1, 2, 8, 7])
print(a)