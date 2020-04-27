# -*- encoding: utf-8 -*-
"""
@File    : 多进程.py
@Time    : 2020/4/27 14:42
@Author  : zwt
@git   : 
@Software: PyCharm
"""

"""
多进程没有共享的状态，改动仅限于当前进程内部
"""
import time
import random
from multiprocessing import Process
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 8080))
server.listen(5)


def piao(name):
    print('%s piaoing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s piao end' % name)


def talk(conn):
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            conn.send(msg.upper())
        except Exception:
            break


if __name__ == '__main__':
    # p1 = Process(target=piao, args=('egon',))
    # p2 = Process(target=piao, args=('alex',))
    #
    # p1.start()
    # p2.start()
    # print('主线程')

    while True:
        conn, client_addr = server.accept()
        p = Process(target=talk, args=(conn))
        p.start()