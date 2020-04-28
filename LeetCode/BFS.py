# -*- encoding: utf-8 -*-
"""
@File    : BFS.py
@Time    : 2020/4/28 11:26
@Author  : zwt
@git   : 
@Software: PyCharm
"""

"""
# 计算从起点 start 到终点 target 的最近距离
def BFS(start, target):
    q = queue.Queue()  # 核心数据结构
    visited = set() # 避免走回头路

    q.put(start) # 将起点加入队列
    visited.add(start)
    int step = 0 # 记录扩散的步数

    while not q.empty():
        int sz = q.qsize()
        # 将当前队列中的所有节点向四周扩散 
        for i in range(sz):
            cur = q.get()
            # 划重点：这里判断是否到达终点 
            if cur == target
                return step
            # 将 cur 的相邻节点加入队列 
            for x in cur:
                if (x not in visited):
                    q.put(x)
                    visited.add(x)
        # 划重点：更新步数在这里 
        step += 1
"""

import queue


def min_depth(root):
    if root is None:
        return 0
    q = queue.Queue()
    q.put(root)
    depth = 1
    while not q.empty():
        sz = q.qsize()
        for i in range(sz):
            cur = q.get()
            if cur.left is None and cur.right is None:
                return depth

            if cur.left is not None:
                q.put(cur.left)
            if cur.right is not None:
                q.put(cur.right)
        depth += 1
    return depth

