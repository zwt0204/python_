# -*- encoding: utf-8 -*-
"""
@File    : MergeSort.py
@Time    : 2019/12/7 10:50
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Merge:

    def __init__(self):
        super(Merge, self).__init__()

    def temp(self, a, b):
        c = []
        h = j = 0
        while j < len(a) and h < len(b):
            if a[j] < b[h]:
                c.append(a[j])
                j += 1
            else:
                c.append(b[h])
                h += 1
        if j == len(a):
            for i in b[h:]:
                c.append(i)
        else:
            for i in a[j:]:
                c.append(i)
        return c

    def run(self, data):
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.run(data[:mid])
        right = self.run(data[mid:])
        return self.temp(left, right)


model = Merge()
a = model.run([3, 1, 2, 8, 7, 3, 2, 1, 0, 9, 0, 10, 60, 13, 56, 78])
print(a)