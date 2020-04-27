# -*- encoding: utf-8 -*-
"""
@File    : 动态规划.py
@Time    : 2020/4/26 16:18
@Author  : zwt
@git   : 
@Software: PyCharm
"""
"""
重叠子问题
最优子结构
状态转移方程
时间复杂度为：子问题个数*子问题复杂度
"""
from datetime import datetime
import time


def helper(temp, n):
    if n == 1 or n == 2:
        return 1
    if temp[n] != 0:
        return temp[n]
    temp[n] = helper(temp, n - 1) + helper(temp, n - 2)
    return temp[n]


def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_2(n):
    if n < 1:
        return 0
    temp = [0] * (n + 1)
    return helper(temp, n)


def fib_3(n):
    temp = [0] * (n + 1)
    temp[1] = temp[2] = 1
    for i in range(3, n + 1):
        temp[i] = temp[i - 1] + temp[i - 2]
    return temp[n]


def fib_4(n):
    if n == 1 or n == 2:
        return 1
    prev = curr = 1
    for i in range(3, n + 1):
        sum = prev + curr
        prev = curr
        curr = sum
    return curr


def coinch(coins, amount):
    # 最多为amount，初始化为amount+1相当于无穷大
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(len(dp)):
        for coin in coins:
            if i - coin < 0:
                continue
            else:
                dp[i] = min(dp[i], 1 + dp[i - coin])

    if dp[amount] == amount + 1:
        return -1
    else:
        return dp[amount]


def coin_start(coins, amount):
    def dp(n):
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = n + 1
        for coin in coins:
            subp = dp(n - coin)
            if subp == -1:
                continue
            res = min(res, 1 + subp)
        if res != (n + 1):
            return res
        return -1

    return dp(amount)


def coin_memo(coins, amount):
    memo = dict()

    def dp(n):
        if n in memo:
            return memo[n]
        if n == 0:
            return 0
        if n < 0:
            return -1
        res = n + 1
        for coin in coins:
            subn = dp(n - coin)
            if subn == -1:
                continue
            res = min(res, 1 + subn)
        # 记入备忘录
        if res != (n + 1):
            memo[n] = res
        else:
            memo[n] = -1
        return memo[n]

    return dp(amount)


if __name__ == '__main__':
    # start = datetime.now()
    start = time.time()
    # a = fib(30)
    # a = fib_4(20)
    # end = datetime.now()

    print(coin_memo([1, 5, 5], 10))
    end = time.time()
    print((end - start) * 1000)
