# -*- encoding: utf-8 -*-
"""
@File    : linked_list.py
@Time    : 2019/12/13 16:24
@Author  : zwt
@git   : 
@Software: PyCharm
"""


class Node():
    """创建节点"""

    def __init__(self, data):
        super().__init__(data)
        self.data = data
        self.next = None


class LinkedList(object):
    """创建列表"""

    def __init__(self):
        """初始化列表"""
        self.head = None
        self.tail = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.head is None

    def append(self, data):
        """追加元素"""
        node = Node(data)  # 把Node类实例化得到一个node对象
        if self.head is None:
            # 如果链表为空，则将head和tail都指向node，即将元素设置为第一个节点
            self.head = node
            self.tail = node
        else:
            # 如果链表非空，则将tail节点和上一个节点的next均指向当前node
            self.tail.next = node
            self.tail = node

    def iter(self):
        """遍历链表"""
        # 如果链表为空，则返回None
        if not self.head:
            return
        cur = self.head
        yield cur.data  # 当前节点data数据的生成器
        while cur.next:
            cur = cur.next  # 当前节点指向下一个节点并遍历
            yield cur.data  # 当前节点data数据的生成器

    def insert(self, idx, value):
        """插入元素"""
        cur = self.head
        cur_idx = 0
        if cur is None:
            raise Exception('The linked_list is empty')
        while cur_idx < idx - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node

    def remove(self, idx):
        """删除元素"""
        cur = self.head
        cur_idx = 0
        if self.head is None:  # 空链表时
            raise Exception('The linked_list is empty')
        while cur_idx < idx - 1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        if idx == 0:  # 当删除第一个节点时
            self.head = cur.next
            cur = cur.next
            return
        if self.head is self.tail:  # 当只有一个节点的链表时
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next is None:  # 当删除的节点是链表最后一个节点时
            self.tail = cur

    def size(self):
        """统计元素个数"""
        cur = self.head
        count = 0
        if cur is None:
            raise Exception('The linked_list is empty')
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def search(self, item):
        """查找指定元素"""
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.data == item:
                found = True
            else:
                cur = cur.next
        return found


if __name__ == '__main__':
    link_list = LinkedList()  # 实例化
    print(link_list.is_empty())  # 判断是否为空
    for i in range(15):
        link_list.append(i)  # 追加15个元素
    print(link_list.size())  # 元素个数
    print(link_list.is_empty())  # 判断是否为空
    link_list.insert(5, 1000)  # 插入一个元素：1000
    print(link_list.size())  # 元素个数
    link_list.remove(0)  # 删除第一个元素
    print(link_list.size())  # 元素个数
    print(link_list.search(10))  # 查找是否存在元素10

    for node in link_list.iter():
        print(f'node is {node}')  # 遍历元素
