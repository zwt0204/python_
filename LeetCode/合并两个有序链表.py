# -*- encoding: utf-8 -*-
"""
@File    : 合并两个有序链表.py
@Time    : 2020/2/28 13:08
@Author  : zwt
@git   : 
@Software: PyCharm
"""
"""
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1:
        return l2  # 终止条件，直到两个链表都空
    if not l2:
        return l1
    if l1.val <= l2.val:  # 递归调用
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
