#!/user/bin/env python
# coding=utf-8
"""
@file: config.py
@author: zwt
@time: 2020/11/10 16:24
@desc: 
"""
from elasticsearch import Elasticsearch


ELASTICSEARCH_DATABASES = {
    'hosts': [{'host': '127.0.0.1', 'port': '9200'}],
    'index': 'graphstore',
}
es = Elasticsearch(**ELASTICSEARCH_DATABASES)