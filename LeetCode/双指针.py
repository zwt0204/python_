# -*- encoding: utf-8 -*-
"""
@File    : 双指针.py
@Time    : 2020/4/28 10:17
@Author  : zwt
@git   : 
@Software: PyCharm
"""

"""
1. 快慢指针：链表中的问题
2. 左右指针：数组或者字符串的问题

数组有序就适合用双指针
"""


def has_cycle(head):
    fast = slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False


def detext_cycle(head):
    fast = slow = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    slow = head
    while slow != fast:
        fast = fast.next
        slow = slow.next

    return slow


def find_k(head, k):
    """链表的倒数第k个数"""
    slow = fast = head
    while k != 0:
        fast = fast.next
        k = k - 1
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


def two_sum(nums, target):
    """左右指针"""
    left = 0
    right = len(nums) - 1
    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left+1, right+1]
        elif sum < target:
            left += 1
        elif sum > target:
            right -= 1
    return [-1, -1]


def reverse(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1