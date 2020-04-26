# -*- encoding: utf-8 -*-
"""
@File    : demo_socket.py
@Time    : 2020/4/26 14:52
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import socket

# TCP
# ip_port = ('127.0.0.1', 8081)  # 电话卡
# BUFSIZE = 1024
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 买手机
# s.bind(ip_port)  # 手机插卡
# s.listen(5)  # 手机待机
#
# while True:  # 新增接收链接循环,可以不停的接电话
#     conn, addr = s.accept()  # 手机接电话
#     # print(conn)
#     # print(addr)
#     print('接到来自%s的电话' % addr[0])
#     while True:  # 新增通信循环,可以不断的通信,收发消息
#         msg = conn.recv(BUFSIZE)  # 听消息,听话
#
#         # if len(msg) == 0:break        #如果不加,那么正在链接的客户端突然断开,recv便不再阻塞,死循环发生
#
#         print(msg, type(msg))
#
#         conn.send(msg.upper())  # 发消息,说话
#
#     conn.close()  # 挂电话
#
# s.close()  # 手机关机

# UDP
# ip_port = ('127.0.0.1', 8081)
# udp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 买手机
# udp_server_sock.bind(ip_port)
#
# while True:
#     qq_msg, addr = udp_server_sock.recvfrom(1024)
#     print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m' % (addr[0], addr[1], qq_msg.decode('utf-8')))
#     back_msg = input('回复消息: ').strip()
#
#     udp_server_sock.sendto(back_msg.encode('utf-8'), addr)

# ntp
from time import strftime

ip_port = ('127.0.0.1', 9000)
bufsize = 1024

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcp_server.bind(ip_port)

while True:
    msg, addr = tcp_server.recvfrom(bufsize)
    print('===>', msg)

    if not msg:
        time_fmt = '%Y-%m-%d %X'
    else:
        time_fmt = msg.decode('utf-8')
    back_msg = strftime(time_fmt)

    tcp_server.sendto(back_msg.encode('utf-8'), addr)

tcp_server.close()
