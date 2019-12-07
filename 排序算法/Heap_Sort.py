# -*- encoding: utf-8 -*-
"""
@File    : Heap_Sort.py
@Time    : 2019/12/7 12:42
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Heap:

    def __init__(self):
        super(Heap, self).__init__()

    def adjust_heap(self, data, parent, length):
        temp = data[parent]
        child = 2 * parent + 1
        while child < length:
            if child + 1 < length and data[child + 1] < data[child]:
                child += 1
            if temp < data[child]:
                break
            data[parent] = data[child]
            parent = child
            child = 2 * parent + 1
        data[parent] = temp
        return data

    def run(self, data):
        length = len(data)
        # 初始化堆
        for i in range(0, length // 2 + 1)[::-1]:
            data = self.adjust_heap(data, i, length)
        for j in range(1, length)[::-1]:
            data[j], data[0] = data[0], data[j]
            data = self.adjust_heap(data, 0, j)
            print('第%d趟排序:' % (length - j), end='')
            print(data)
        return data


model = Heap()
a = model.run([3, 1, 2, 8, 7])
print(a)