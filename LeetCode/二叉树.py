# -*- encoding: utf-8 -*-
"""
@File    : 二叉树.py
@Time    : 2020/4/28 15:08
@Author  : zwt
@git   : 
@Software: PyCharm
"""

"""
def traverse(root):
    # root 需要做什么？在这做。
    # 其他的不用 root 操心，抛给框架
    traverse(root.left);
    traverse(root.right);
"""

import math


def plus_one(root):
    if root is None:
        return
    root.val += 1
    plus_one(root.left)
    plus_one(root.right)


def is_same_tree(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.val != root2.val:
        return False
    return is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right)


class Solution:

    def isValidBST(self, root):
        return self.isValidBST1(root, None, None)

    def isValidBST1(self, root, min, max):
        if root is None:
            return True
        if min is not None and root.val <= min.val:
            return False
        if max is not None and root.val >= max.val:
            return False
        return self.isValidBST1(root.left, min, root) and self.isValidBST1(root.right, root, max)


def is_in_bst(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return is_in_bst(root.left, target) or is_in_bst(root.right, target)


def insert_data(root, val):
    if root is None:
        return val
    if root.val < val:
        root.right = insert_data(root.right, val)
    if root.val > val:
        root.left = insert_data(root.left, val)
    return root


def get_min(node):
    while node.left is not None:
        node = node.left
    return node


def del_data(root, key):
    if root is None:
        return None
    if root.val == key:
        # 末端节点或者只有一个非空子节点
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        # 有两个子节点，为了不破坏性质需要调整，找到右子树中最小的节点
        minNode = get_min(root.right)
        root.val = minNode.val
        root.right = del_data(root.right, minNode.val)
    elif root.val > key:
        root.left = del_data(root.left, key)
    elif root.val < key:
        root.right = del_data(root.right, key)
    return root


def general_count_node(root):
    """
    计算节点数目
    :param root:
    :return:
    """
    if root is None:
        return 0
    return 1 + general_count_node(root.left) + general_count_node(root.right)


def full_count_node(root):
    h = 0
    while root is not None:
        root = root.left
        h += 1
    return math.pow(2, h) - 1


def all_count_node(root):
    l = r = root
    hl = hr = 0
    while l is not None:
        l = l.left
        hl += 1
    while r is not None:
        r = r.right
        hr += 1
    if hl == hr:
        return math.pow(2, hl) - 1
    return 1 + all_count_node(root.left) + all_count_node(root.right)


























