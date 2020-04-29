# -*- encoding: utf-8 -*-
"""
@File    : 二分法.py
@Time    : 2020/4/27 13:33
@Author  : zwt
@git   : 
@Software: PyCharm
"""
"""
框架：
def binarySearch(nums, target):
    left = 0, right = 0
    while(...):
        mid = (right - left) // 2
        if (nums[mid] == target):
            ...
        else if (nums[mid] < target):
            left = ...
        else if (nums[mid] > target):
            right = ...
    return ...
"""


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (right + left) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            left = mid - 1
        else:
            return mid
    return -1


def left_binary_search(nums, target):
    length = len(nums) - 1
    if length == 0:
        return -1
    left = 0
    right = length
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1

    # 检查越界
    if left >= len(nums) or nums[left] != target:
        return -1
    return left


def right_bin_search(nums, target):
    length = len(nums) - 1
    if length == 0:
        return -1
    left = 0
    right = length
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = right - 1
        elif nums[mid] == target:
            left = mid + 1
        # 检查越界
    if right < 0 or nums[right] != target:
        return -1
    return left


if __name__ == '__main__':
    nums = [2, 6, 8, 8]
    target = 8
    result = left_binary_search(nums, target)
    print(result)