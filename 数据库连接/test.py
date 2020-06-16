# -*- encoding: utf-8 -*-
"""
@File    : test.py
@Time    : 2020/2/25 15:02
@Author  : zwt
@git   : 
@Software: PyCharm
"""
from .mysql_pool import Mysql

# 申请资源
mysql = Mysql()

sqlAll = "select * from answer_time"
result = mysql.getAll(sqlAll)
if result:
    for row in result:
        row["answer"] = str(row["answer"], encoding="utf8")
        print("%s\t%s" % (row["answer"], row["start_day"]))
# sqlAll = ""
# result = mysql.getMany(sqlAll, 2)
# if result:
#     for row in result:
#         print("%s\t%s" % (row["uid"], row["goodsname"]))
#
# result = mysql.getOne(sqlAll)
#
# print("%s\t%s" % (result["uid"], result["goodsname"]))

# 释放资源
mysql.dispose()
