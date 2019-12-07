# -*- encoding: utf-8 -*-
"""
@File    : Insert_Sort.py
@Time    : 2019/12/6 17:35
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Insert:

    def __init__(self):
        super(Insert, self).__init__()

    def run(self, data):
        length = len(data)
        for i in range(1, length):
            x = data[i]
            for j in range(i, -1, -1):
                # j为当前位置，试探j-1的位置
                if x < data[j -1]:
                    data[j] = data[j -1]
                else:
                    # 位置确定为j
                    break
            data[j] = x
        return data


class Insert_2:

    def __init__(self):
        super(Insert_2, self).__init__()

    def run(self, data):
        length = len(data)
        for i in range(1, length):
            x = data[i]
            left = 0
            right = i - 1
            # 待插入的值与已排序区域的中间值比较，不断缩小区域范围，直到left和right相遇。
            while left <= right:
                mid = (left + right) // 2
                if data[mid] > x:
                    right = mid - 1
                else:
                    left = mid + 1
            # 查找出temp应插入的位置后，将left后面的数字均向后移动一位
            j = i - 1
            while j >= left:
                data[j+1] = data[j]
                j -= 1
            # 此时left位置上放置待插入的数字
            data[left] = x
        return data


model = Insert_2()
a = model.run([3, 1, 2, 8, 7, 3, 2, 1, 0, 9, 0, 10, 60, 13, 56, 78])
print(a)


