# -*- encoding: utf-8 -*-
"""
@File    : 前缀和技巧.py
@Time    : 2020/4/30 15:22
@Author  : zwt
@git   : 
@Software: PyCharm
"""

"""
pre_sum的含义就是前i项的和。如果要求[i,j]。那么只需要计算pre_sum[j+1] - pre_sum[i]
"""


def sum_k(nums, k):
    n = len(nums)
    sum = [0 for _ in range(n+1)]
    sum[0] = 0
    for i in range(n):
        sum[i+1] = sum[i] + nums[i]
    result = 0
    for i in range(n):
        for j in range(i):
            if sum[i] - sum[j] == k:
                result += 1
    return result


def sum_k_2(nums, k):
    dict = {}
    n = len(nums)
    sum_r = 0
    result = 0
    for i in range(n):
        sum_r = sum_r + nums[i]
        temp = sum_r - k
        if dict.get(temp):
            result += dict.get(temp)
        dict[sum_r] = dict.get(sum_r, 0) + 1
    return result


if __name__ == '__main__':
    data = [1, 2, 3, 5, 8, 9, 6, 1, 2, 3, 4]
    print(sum_k_2(data, 10))