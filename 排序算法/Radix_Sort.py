# -*- encoding: utf-8 -*-
"""
@File    : Radix_Sort.py
@Time    : 2019/12/7 14:03
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Radix:

    def __init__(self):
        super(Radix, self).__init__()

    def run(self, data):
        # 记录当前正在排哪一位，最低位为1
        i = 0
        # 最大值
        max_num = max(data)
        # 记录最大值的位数
        j = len(str(max_num))
        while i < j:
            # 初始桶的数量
            bucket_list = [[] for _ in range(10)]
            for x in data:
                # 找到位置放入桶数组
                bucket_list[int(x / (10 ** i)) % 10].append(x)
            data.clear()
            for x in bucket_list:
                for y in x:
                    data.append(y)
            i += 1
        return data


model = Radix()
a = model.run([3, 1, 2, 8, 7])
print(a)