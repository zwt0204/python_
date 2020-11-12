#!/user/bin/env python
# coding=utf-8
"""
@file: base_es.py
@author: zwt
@time: 2020/11/6 17:45
@desc: 
"""
import traceback
import logging
from elasticsearch import exceptions
from copy import deepcopy
from .config import es

_logger = logging.getLogger()


class AnalyzerType(object):
    """分析器"""
    keyword = 'keyword'
    split_ana = 'split_ana'
    jieba_ana = 'jieba_ana'


class FiledTpye(object):
    """"""
    FLOAT = 'float'
    TEXT = 'text'
    KEYWORD = 'keyword'
    INTEGER = 'integer'
    SHORT = 'short'
    BYTE = 'byte'
    BOOLEAN = 'boolean'


class ElasticsearchField(object):
    """"""
    field_type = FiledTpye.TEXT
    analyzer = None
    descrip = None

    def __init__(self, **kwargs):
        super(ElasticsearchField, self).__init__()
        for k, v in kwargs.items():
            if v:
                setattr(self, k, v)
        if not self.field_type:
            raise Exception('未发现字段类型')

    def to_dict(self):
        """"""
        res = {}
        if self.field_type:
            res['type'] = self.field_type
        if self.analyzer:
            res['analyzer'] = self.analyzer
        return res


class BooleanField(ElasticsearchField):
    """"""
    field_type = FiledTpye.BOOLEAN


class FloatField(ElasticsearchField):
    """"""
    field_type = FiledTpye.FLOAT


class IntegerField(ElasticsearchField):
    """"""
    field_type = FiledTpye.INTEGER


class KeywordField(ElasticsearchField):
    """"""
    field_type = FiledTpye.KEYWORD

    def __init__(self, split_char=None, **kwargs):
        super(KeywordField, self).__init__(**kwargs)
        self.split_char = split_char


class ElasticModel(object):
    """elasticsearch 基类"""
    number_of_shards = 1  # 分片数量
    number_of_replicas = 1  # 副本数量
    split_parttern = '[,|-]+'
    _index_name = None  # 索引名称

    def __init__(self):
        super(ElasticModel, self).__init__()
        self._fields = {}
        for k, v in self.__class__.__dict__.items():
            if issubclass(type(v), ElasticsearchField):
                self._fields[k] = v
        self.es = es

    @property
    def feild_keys(self):
        return self._fields.keys()

    @property
    def _mappings(self):
        return NotImplementedError

    @property
    def _settings(self):
        return NotImplementedError

    def create(self, index_name=None):
        """创建索引"""
        index_name = index_name or self.index_name
        try:
            body = {}
            body.update(self._mappings)
            body.update(self._settings)
            self.es.indices.create(index_name, body)
        except exceptions.RequestError as e:
            _logger.warning('索引已经存在， 请勿重复创建')
            _logger.warning(u" %s ", str(traceback.format_exc()))

    def delete(self, index_name=None):
        """删除索引"""
        index_name = index_name or self.index_name
        try:
            self.es.indices.delete(index_name)
        except exceptions.NotFoundError as e:
            _logger.warning('索引不存在，无法删除')

    def reindex(self, index_name=None):
        """删除然后重建索引"""
        index_name = index_name or self.index_name
        self.delete(index_name)
        self.create(index_name)

    def doc_create(self, index_name, doc_id, body):
        """"""

    def body_fix(self, data):
        """"""
        res = deepcopy(data)
        feild_list = self._fields.keys()
        for k, v in data.items():
            if k in feild_list:
                if self._fields[k].field_type == FiledTpye.BOOLEAN and not isinstance(v, bool):
                    if isinstance(v, str) or isinstance(v, bytes):
                        res[k] = False if float(v) == 0.0 else True
                    elif isinstance(v, int) or isinstance(v, float):
                        res[k] = True if v else False
                elif self._fields[k].field_type == FiledTpye.FLOAT:
                    res[k] = float(v)
                elif isinstance(v, list) or isinstance(v, tuple):
                    res[k] = list(set(v))
        return res

    def db_to_es(self, *args, **kwargs):
        """从db 到 es中"""
        return NotImplementedError

    @property
    def index_name(self):
        if not self._index_name:
            raise Exception('请定义索引名称')
        res = '{}_{}'.format(ELASTICSEARCH_DATABASES['index_prefix'], self._index_name)
        return res


def to_list(s, split_char=' '):
    """"""
    res = []
    if s:
        for i in s.split(split_char):
            if i:
                res.append(i)
    return res


def split_merge(key=None, dt=None):
    """"""
    res = []
    for k in key:
        res += to_list(dt.get(k, None))
    return res


def insert_no_empty(data, key, value):
    if value:
        data[key] = value