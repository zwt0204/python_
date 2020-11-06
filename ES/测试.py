#!/user/bin/env python
# coding=utf-8
"""
@file: 测试.py
@author: zwt
@time: 2020/11/3 16:44
@desc: 
"""
from elasticsearch import Elasticsearch
import json

es = Elasticsearch()  # 默认连接本地elasticsearch
# print(es)
# es = Elasticsearch(['xxx.xx.xx.xx:9200'])  # 连接指定9200端口
# es = Elasticsearch(
#     ["IP地址"], # 连接集群，以列表的形式存放各节点的IP地址
#     sniff_on_start=True,    # 连接前测试
#     sniff_on_connection_fail=True,  # 节点无响应时刷新节点
#     sniff_timeout=60)    # 设置超时时间
# 除开链接指定的IP地址外,其他的都可以不设置,使用默认值
doc = {
     'article_id': '1',
     'user_id': '2',
     'title': '周报'
   }

# es.index(index='articles', doc_type='article', body=doc, id='1')

# query = {
#     "query":
#         {
#             "match":
#                 {
#                     "title": "周报"
#                 }
#         }
# }
#
# query = {
#     "query":
#         {
#             "match_all": {}
#         }
# }

query = {
    "query": {
        "match": {
            "ngram_question": "今天天气如何"
        }
    }
}

ret = es.search(index='data_server_knowledge', doc_type='_doc', body=query)
print(ret)