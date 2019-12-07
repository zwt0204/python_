# -*- encoding: utf-8 -*-
"""
@File    : Shell_Sort.py
@Time    : 2019/12/7 10:06
@Author  : zwt
@git   : 
@Software: PyCharm
"""
from gaps import sedgewick_gaps


class Shell:

    def __init__(self):
        super(Shell, self).__init__()

    def run(self, data):
        length = len(data)
        if length <= 1:
            return
        # 初始步长
        gap = length // 2
        # 最后一次步长为1，然后整个希尔排序结束
        while gap > 0:
            """
            想象，以步长gap将原始序列划分为gap个待排序序列，对每个序列使用普通的插入排序进行排序
            序列1：[lenght[0], lenght[gap], length[gap*2]...]
            序列2：[length[1], length[gap + 1], length[1 + 2 *gap,....]]
            """
            # "未排序序列" 的第1个元素分别是L[gap], L[1+gap], L[2+gap] ... ，所以变量 i 表示的下标是 gap, 1+gap, 2+gap ...
            for i in range(gap, length):
                temp = data[i]
                j = i
                while j >= gap and temp < data[j - gap]:
                    data[j] = data[j - gap]
                    j -= gap
                data[j] = temp
            # 新的步长
            gap = gap // 2
        return data


class Shell_1:

    def __init__(self):
        super(Shell_1, self).__init__()

    def run(self, data):
        """
        步长序列使用 Sedgewick 提出的[1, 5, 19, 41, 109, 209, 505, 929 ...]，此时时间复杂度为 O(n (logn)^2)
        :return:
        """
        length = len(data)
        gaps = sedgewick_gaps(length)
        # 将gaps生成器对象转换成列表，再倒序: [41, 19, 5, 1]
        for gap in reversed(list(gaps)):
            for i in range(gap, length):
                temp = data[i]
                j = i
                while j >= gap and temp < data[j - gap]:
                    data[j] = data[j - gap]
                    j -= gap
                data[j] = temp
        return data


model = Shell_1()
a = model.run([3, 1, 2, 8, 7, 3, 2, 1, 0, 9, 0, 10, 60, 13, 56, 78])
print(a)