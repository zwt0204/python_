# -*- encoding: utf-8 -*-
"""
@File    : Config.py
@Time    : 2020/2/25 14:59
@Author  : zwt
@git   : 
@Software: PyCharm
"""

"""
mincached ：启动时开启的空连接数量
maxcached ：连接池最大可用连接数量
maxshared ：连接池最大可共享连接数量
maxconnections ：最大允许连接数量
maxusage ：单个连接最大复用次数
blocking ：达到最大数量时是否阻塞
"""
DBHOST = "127.0.0.1"
DBPORT = 3306
DBUSER = "root"
DBPWD = "123456"
DBNAME = "test"
DBCHAR = "utf8"
mincached = 1
maxcached = 20