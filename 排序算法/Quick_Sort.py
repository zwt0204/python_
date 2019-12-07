# -*- encoding: utf-8 -*-
"""
@File    : Quick_Sort.py
@Time    : 2019/12/7 11:20
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Quick:

    def __init__(self):
        super(Quick, self).__init__()

    def run(self, data):
        length = len(data)
        if length < 2:
            return data
        # 选取基准，随便选那个都可以,选中间便于理解
        mid = data[length // 2]
        # 定义基准值在左右两个数列
        left, right = [], []
        # 从原始数组中移除基准值
        data.remove(mid)
        for item in data:
            # 大于基准放右边
            if item >= mid:
                right.append(item)
            else:
                left.append(item)
        # 使用迭代进行比较
        return self.run(left) + [mid] + self.run(right)


class Quick_2:

    def __init__(self):
        super(Quick_2, self).__init__()

    def run(self, data, left, right):
        if left >= right:
            return data
        stack = [left, right]
        while stack:
            low = stack.pop(0)
            high = stack.pop(0)
            if high <= low:
                continue
            pivot = data[high]
            i = low - 1
            for j in range(low, high+1):
                if data[j] <= pivot:
                    i += 1
                    data[i], data[j] = data[j], data[i]
            stack.extend([low, i - 1, i + 1, high])
        return data


model = Quick_2()
a = model.run([3, 1, 2, 8, 7], 0, 4)
print(a)