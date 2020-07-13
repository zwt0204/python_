# -*- encoding: utf-8 -*-
"""
@File    : 编辑距离.py
@Time    : 2020/7/13 16:29
@Author  : zwt
@git   : 
@Software: PyCharm
"""


def edit_distence(str1, str2):
    """递归"""
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1 == str2:
        return 0

    if str1[len(str1) - 1] == str2[len(str2) - 1]:
        d = 0
    else:
        d = 1

    return min(edit_distence(str1, str2[:-1]) + 1,
               edit_distence(str1[:-1], str2) + 1,
               edit_distence(str1[:-1], str2[:-1]) + d)


def edit_(str1, str2):
    """动态规划"""
    matrix = [[i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                d = 0
            else:
                d = 1

            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + d)

    return matrix[len(str1)][len(str2)]


if __name__ == '__main__':
    # print(edit_("xxc", "xyz"))
    import numpy as np
    temp = np.zeros((4, 4), dtype=np.int)
    temp[0] = np.arange(4)
    temp[:, 0] = np.arange(4)
    print(temp)