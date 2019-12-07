# -*- encoding: utf-8 -*-
"""
@File    : Bucket_Sort.py
@Time    : 2019/12/7 13:48
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Bucket:

    def __init__(self):
        super(Bucket, self).__init__()

    def run(self, data):
        # 选择一个最大的数
        max_num = max(data)
        # 创建一个元素全是0的列表，当做桶
        bucket = [0] * (max_num + 1)
        # 把所有元素放入桶中，即把对应的元素个数加1
        for i in data:
            bucket[i] += 1
        # 存储排序好的元素
        sort_num = []
        # 取出桶中的元素
        for j in range(len(bucket)):
            if bucket[j] != 0:
                for y in range(bucket[j]):
                    sort_num.append(j)
        return sort_num


model = Bucket()
a = model.run([3, 1, 2, 8, 7])
print(a)