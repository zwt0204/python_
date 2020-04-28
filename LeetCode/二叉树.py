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

