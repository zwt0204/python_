# -*- encoding: utf-8 -*-
"""
@File    : thread_1.py
@Time    : 2019/12/9 13:28
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import threading
import datetime
import math


def run(name):
    print(len(name))


list = []
with open('data.txt', 'r', encoding='utf8') as f:
    for line in f.readlines():
        list.append(line.strip())

threads = []
files_list = len(list)
# 每个线程处理数量
num_data = 1000
# 线程数
num_threads = math.ceil(files_list / num_data)

# 创建线程
for i in range(0, num_threads):
    t = threading.Thread(target=run, args=(list[num_data*i: num_data*(i+1)],))
    threads.append(t)

if __name__ == '__main__':
    t1 = datetime.datetime.now()
    # 启动线程
    for i in range(num_threads):
        threads[i].start()
    for i in range(num_threads):
        threads[i].join()

    # 主线程
    print(datetime.datetime.now() - t1)