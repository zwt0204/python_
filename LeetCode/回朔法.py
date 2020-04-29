# -*- encoding: utf-8 -*-
"""
@File    : 回朔法.py
@Time    : 2020/4/27 10:42
@Author  : zwt
@git   : 
@Software: PyCharm
"""
"""
回溯问题就是决策树的遍历过程
1. 路径：做出的选择
2. 选择列表：当前可以做的选择
3. 结束条件：到达决策树底层，无法再做出选择的条件
框架：
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""
# 路径：记录在 track 中
# 选择列表：nums 中不存在于 track 的那些元素
# 结束条件：nums 中的元素全都在 track 中出现

from sys import stdout


def permutations(arr, position, end):
    if position == end:
        stdout.writelines(str(arr))
    else:
        for index in range(position, end):
            # 做选择
            arr[index], arr[position] = arr[position], arr[index]
            permutations(arr, position + 1, end)
            # 撤回选择
            arr[index], arr[position] = arr[position], arr[index]  # 还原到交换前的状态，为了进行下一次交换


# 检测（x,y）这个位置是否合法（不会被其他皇后攻击到）
def is_attack(queue, x, y):
    for i in range(x):
        if queue[i] == y or abs(x - i) == abs(queue[i] - y):
            return True
    return False


# 按列来摆放皇后
def put_position(n, queue, col):
    for i in range(n):
        if not is_attack(queue, col, i):
            queue[col] = i
            if col == n - 1:    # 此时最后一个皇后摆放好了，打印结果。
                print(queue)
            else:
                put_position(n, queue, col + 1)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    permutations(arr, 0, len(arr))
    # print(stdout)

    # 这里是n 就是n皇后
    # n = 8
    # # 存储皇后位置的一维数组，数组下标表示皇后所在的列，下标对应的值为皇后所在的行。
    # queue = [None for i in range(n)]
    # put_position(n, queue, 0)