# -*- encoding: utf-8 -*-
"""
@File    : demo2_scoket.py
@Time    : 2020/4/26 15:02
@Author  : zwt
@git   : 
@Software: PyCharm
"""
import socket

# TCP
# ip_port = ('127.0.0.1', 8081)
# BUFSIZE = 1024
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s.connect_ex(ip_port)  # 拨电话
#
# while True:  # 新增通信循环,客户端可以不断发收消息
#     msg = input('>>: ').strip()
#     if len(msg) == 0:
#         continue
#     s.send(msg.encode('utf-8'))  # 发消息,说话(只能发送字节类型)
#
#     feedback = s.recv(BUFSIZE)  # 收消息,听话
#     print(feedback.decode('utf-8'))
#
# s.close()  # 挂电话

# UDP

# BUFSIZE = 1024
# udp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# qq_name_dic = {
#     '狗哥alex': ('127.0.0.1', 8081),
#     '瞎驴': ('127.0.0.1', 8081),
#     '一棵树': ('127.0.0.1', 8081),
#     '武大郎': ('127.0.0.1', 8081),
# }
#
# while True:
#     qq_name = input('请选择聊天对象: ').strip()
#     while True:
#         msg = input('请输入消息,回车发送: ').strip()
#         if msg == 'quit': break
#         if not msg or not qq_name or qq_name not in qq_name_dic: continue
#         udp_client_socket.sendto(msg.encode('utf-8'), qq_name_dic[qq_name])
#
#         back_msg, addr = udp_client_socket.recvfrom(BUFSIZE)
#         print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m' % (addr[0], addr[1], back_msg.decode('utf-8')))
#
# udp_client_socket.close()

# ntp
from socket import *

ip_port = ('127.0.0.1', 9000)
bufsize = 1024

tcp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('请输入时间格式(例%Y %m %d)>>: ').strip()
    tcp_client.sendto(msg.encode('utf-8'), ip_port)
    data = tcp_client.recv(bufsize)
    print(data.decode('utf-8'))

tcp_client.close()
