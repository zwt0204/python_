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


class Heap_1:

    def __init__(self):
        super(Heap_1, self).__init__()

    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i] < arr[l]:
            largest = l
        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def run(self, arr):
        n = len(arr)

        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            # 交换
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
        return arr


model = Heap_1()
a = model.run([3, 1, 2, 8, 7])
print(a)