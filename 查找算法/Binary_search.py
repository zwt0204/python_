# -*- encoding: utf-8 -*-
"""
@File    : Binary_search.py
@Time    : 2019/11/15 17:24
@Author  : zwt
@git   : 
@Software: PyCharm
"""


def bs(alist, target):
    """
    非递归
    :param alist:
    :param target:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > target:
            last = mid - 1
        elif alist[mid] < target:
            first = mid + 1
        else:
            return True
    return False


def binarySearch(arr, min, max, key):
    mid = int((max + min)/2)
    if key < arr[mid]:
        return binarySearch(arr, min, mid-1, key)
    elif key > arr[mid]:
        return binarySearch(arr, mid+1, max, key)
    elif key == arr[mid]:
        print("找到{0}了！是第{1}个数字！".format(key, mid))
    else:
        print("没找到！")


if __name__ == '__main__':
    lis = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    result = binarySearch(lis, 0, 8, 66)