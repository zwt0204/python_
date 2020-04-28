# -*- encoding: utf-8 -*-
"""
@File    : 滑动窗口.py
@Time    : 2020/4/27 16:38
@Author  : zwt
@git   : 
@Software: PyCharm
"""
"""
/* 滑动窗口算法框架 */
void slidingWindow(string s, string t) 
    unordered_map<char, int> need, window
    for (char c : t) need[c]++

    int left = 0, right = 0
    int valid = 0 
    while (right < s.size()) 
        #c 是将移入窗口的字符
        char c = s[right]
        #右移窗口
        right++
        #进行窗口内数据的一系列更新
        ...

        /*** debug 输出的位置 ***/
        printf("window: [%d, %d)\n", left, right)
        /********************/

        #判断左侧窗口是否要收缩
        while (window needs shrink) 
            #d 是将移出窗口的字符
            char d = s[left]
            #左移窗口
            left++
            #进行窗口内数据的一系列更新
            ...
        
    

"""


def min_window(s, t):
    need, window = dict(), dict()
    for c in t:
        if c in need:
            need[c] += 1
        else:
            window[c] = 0
            need[c] = 1
    left = 0
    right = 0
    valid = 0
    # 记录最小覆盖子串的起始索引及长度
    start = 0
    leng = float("inf")
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        # 右移窗口
        right += 1
        # 进行窗口内数据的一系列更新
        if need.get(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        # 判断左侧窗口是否要收缩
        while valid == len(need):
            # 在这里更新最小覆盖子串
            if right - left < leng:
                start = left
                leng = right - left

            # d 是将移出窗口的字符
            d = s[left]
            # 左移窗口
            left += 1
            # 进行窗口内数据的一系列更新
            if need.get(d):
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1

    # 返回最小覆盖子串
    if leng == len(s):
        return ""
    return s[start:start + leng]


def find_a(s, t):
    need, window = dict(), dict()
    for c in t:
        if c in need:
            need[c] += 1
        else:
            window[c] = 0
            need[c] = 1
    left = 0
    right = 0
    valid = 0
    res = []
    while right < len(s):
        # c 是将移入窗口的字符
        c = s[right]
        # 右移窗口
        right += 1
        # 进行窗口内数据的一系列更新
        if need.get(c):
            window[c] += 1
            if window[c] == need[c]:
                valid += 1

        # 判断左侧窗口是否要收缩
        while right - left >= len(t):
            if valid == len(need):
                res.append(left)

            d = s[left]
            # 左移窗口
            left += 1
            # 进行窗口内数据的一系列更新
            if need.get(d):
                if window[d] == need[d]:
                    valid -= 1
                window[d] -= 1
    return res


def sub_length(s):
    window = dict()
    for c in s:
        window[c] = 0
    left = 0
    right = 0
    res = 0
    while right < len(s):
        c = s[right]
        right += 1
        window[c] += 1
        while window[c] > 1:
            d = s[left]
            left += 1
            window[d] -= 1
    res = max(res, right - left)

    return res


if __name__ == '__main__':
    S = "ADODB"
    T = "DO"
    a = sub_length(S)
    print("答案:", a)
