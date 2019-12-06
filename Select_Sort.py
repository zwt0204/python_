# -*- encoding: utf-8 -*-
"""
@File    : Select_Sort.py
@Time    : 2019/12/5 16:07
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Select:

    def __init__(self):
        super().__init__()

    def run(self, data):
        length = len(data)
        for i in range(length - 1):
            minIndex = i
            for j in range(i + 1, length):
                if data[j] < data[minIndex]:
                    minIndex = j
            temp = data[i]
            data[i] = data[minIndex]
            data[minIndex] = temp
        return data


class Select_1:

    def __init__(self):
        super().__init__()

    def run(self, data_list):
        count = 0
        length = len(data_list)
        for i in range(length - 1):
            print(data_list)  # 打印每一次选择后的结果
            min_index = i  # 存储最小值的下标，以便最后交换
            for j in range(i + 1, length):
                count += 1
                if data_list[min_index] > data_list[j]:
                    min_index = j
            if min_index != i:  # 说明需要交换，否则不需要自己自己交换
                tmp = data_list[i]
                data_list[i] = data_list[min_index]
                data_list[min_index] = tmp
        print(f"总循环次数为 {count}")
        return data_list


class Select_2:

    def __init__(self):
        super().__init__()

    def run(self, data_list):
        count = 0
        length = len(data_list)
        for i in range(length - 1):
            # print(data_list)  # 打印每一次选择后的结果
            min_index = i  # 存储最小值的下标
            max_index = length - i - 1  # 最大值的下标，以便最后交换

            for j in range(i + 1, length - i - 1):
                count += 1
                if data_list[min_index] > data_list[j]:
                    min_index = j
                if data_list[max_index] < data_list[j]:
                    max_index = j

                # 退出条件
            if min_index + 1 == max_index:
                break

            # 前面的数据与最小值交换
            if min_index != i:  # 说明需要交换，否则不需要自己自己交换
                tmp = data_list[i]
                data_list[i] = data_list[min_index]
                data_list[min_index] = tmp

            # 后面的数据与最大值交换
            if max_index != length - i - 1:  # 说明需要交换，否则不需要自己与自己交换
                tmp = data_list[length - i - 1]
                data_list[length - i - 1] = data_list[max_index]
                data_list[max_index] = tmp

        print(f"总循环次数为 {count}")
        return data_list


model = Select_2()
a = model.run([3, 1, 2, 8, 7, 3, 2, 1, 0, 9, 0, 10, 60, 13, 56, 78])
print(a)