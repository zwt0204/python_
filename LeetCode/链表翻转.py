# -*- encoding: utf-8 -*-
"""
@File    : 链表翻转.py
@Time    : 2020/4/28 19:13
@Author  : zwt
@git   : 
@Software: PyCharm
"""


def linked_reverse(head):
    if head is None:
        return head
    last = linked_reverse(head.next)
    head.next.next = head
    head.next = None
    return last


class Solution(object):

    def reverseBetween(self, head, m, n):

        def reverseN(head, n):
            if n == 1:
                return head
            # 以 head.next 为起点，需要反转前 n - 1 个节点
            last = reverseN(head.next, n - 1)
            successor = head.next.next
            # 以head.next为开头的链表已经完成翻转，那么head.next.next正确指向后继节点
            head.next.next = head
            head.next = successor
            return last

        if m == 1:
            return reverseN(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head
