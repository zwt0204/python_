# -*- encoding: utf-8 -*-
"""
@File    : 用栈实现队列.py
@Time    : 2020/4/29 13:41
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class MyQueue(object):

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        """
        get the front element
        """
        if self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2[-1]

    def empty(self):
        return self.s1 and self.s2


class MyStack(object):

    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        return self.queue.pop()

    def top(self):
        return self.queue[-1]

    def empty(self):
        if self.queue:
            return True
        else:
            return False