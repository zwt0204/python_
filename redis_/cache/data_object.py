#!/user/bin/env python
# coding=utf-8
"""
@file: data_object.py
@author: zwt
@time: 2020/10/30 17:35
@desc: 
"""
import json
import uuid
from redis import Redis
import logging
from .config import redis_pool
from ..utils import DataEncoder

_logger = logging.getLogger()


class DataObject(object):

    def __init__(self, session_id, data=""):
        super(DataObject, self).__init__()
        ss_id = session_id or ''
        self.session_id = 'session:' + str(ss_id)
        self.data = data
        # 加载数据
        self.init_from_redis()

    def init_from_redis(self):
        """从redis中获取数据初始化session"""
        if not self.short_session_id:
            self.generate_session_id()
            return
        data = self.connect.get(self.session_id)
        if data:
            self.loads(data)
        else:
            self.generate_session_id()

    def generate_session_id(self):
        _logger.warning('输入的session_id 不存在，重新生成 session_id')
        self.session_id = 'session:' + uuid.uuid1().hex

    @property
    def short_session_id(self):
        """"""
        return self.session_id[8:]

    @property
    def connect(self):
        """redis数据库链接"""
        return Redis(connection_pool=redis_pool)

    def dumps(self, json_dumps=False):
        """
        生成数据字典
        :return:
        """
        res = {
            "data": self.data
        }
        if json_dumps:
            res = json.dumps(res, cls=DataEncoder)
        return res

    def loads(self, data, json_loads=False):
        """
        恢复数据
        :param data:
        :param json_loads:
        :return:
        """
        if json_loads:
            data = json.loads(data)
        self.data = data

    def save(self):
        """保存"""

        session_dict = self.dumps(json_dumps=True)
        self.connect.set(name=self.session_id, value=session_dict)

    @staticmethod
    def generate_only_id(tag='dialogue'):
        """生成信息对象的唯一id"""
        return '%s:%s' % (tag, uuid.uuid1().hex)

    def delete(self):
        """
        删除本身缓存
        :return:
        """
        self.connect.delete(self.session_id)


