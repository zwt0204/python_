# -*- encoding: utf-8 -*-
"""
@File    : Bubble_Sort.py
@Time    : 2019/12/5 15:08
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Bubble:

    def __init__(self):
        super().__init__()

    def run(self, data):
        for i in range(len(data) - 1):
            for j in range(0, len(data) - 1 - i):
                if data[j] > data[j + 1]:
                    temp = data[j + 1]
                    data[j + 1] = data[j]
                    data[j] = temp
        return data


class Bubble_1:
    """
    提前结束，如果当前轮次跑完没有交换一次，那就直接结束
    """

    def __init__(self):
        super().__init__()

    def run(self, data):
        for i in range(len(data) - 1):
            flag = True
            for j in range(0, len(data) - 1 - i):
                if data[j] > data[j + 1]:
                    temp = data[j + 1]
                    data[j + 1] = data[j]
                    data[j] = temp
                    flag = False
            if flag:
                break
        return data


class Bubble_2:
    """
    只循环无序数据，记录无序数据边界
    """

    def __init__(self):
        super().__init__()

    def run(self, data):
        boundary = len(data) - 1
        lastExchangeIndex = 0
        for i in range(len(data) - 1):
            flag = True
            for j in range(0, boundary):
                if data[j] > data[j + 1]:
                    temp = data[j + 1]
                    data[j + 1] = data[j]
                    data[j] = temp
                    flag = False
                    lastExchangeIndex = j
            boundary = lastExchangeIndex
            if flag:
                break
        return data


model = Bubble_2()
a = model.run([3, 1, 2, 8, 7, 3, 2, 1, 0, 9, 0, 10, 60, 13, 56, 78])
print(a)