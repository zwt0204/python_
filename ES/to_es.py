#!/user/bin/env python
# coding=utf-8
"""
@file: to_es.py
@author: zwt
@time: 2020/11/6 17:54
@desc: 
"""
import logging
from math import ceil
from tqdm import tqdm

from .base_es import ElasticModel, KeywordField, ElasticsearchField, FiledTpye, IntegerField, AnalyzerType

_logger = logging.getLogger()


class KnowledgeQAModel(ElasticModel):
    """"""
    _bulk = 50
    _index_name = 'knowledge'

    qa_id = IntegerField()
    mall_id = KeywordField(descrip='id')
    qa_status = IntegerField(descrip='问题状态')

    question = KeywordField(descrip='问题')
    ngram_question = ElasticsearchField(field_type=FiledTpye.TEXT, analyzer='ngram_ana', descrip='ngram门店搜索')
    match_question = ElasticsearchField(field_type=FiledTpye.TEXT, analyzer=AnalyzerType.jieba_ana, descrip='门店搜索')

    @property
    def _settings(self):
        """"""
        res = {
            "settings": {
                "index": {
                    "number_of_shards": self.number_of_shards,
                    "number_of_replicas": self.number_of_replicas,
                    'max_ngram_diff': 3,
                },
                "analysis": {
                    "filter": {
                        "jieba_stop": {
                            "type": "stop",
                            "stopwords_path": "stopwords/stopwords.txt",
                            # "stopwords": [],
                        }
                    },
                    "analyzer": {
                        "jieba_ana": {
                            "tokenizer": "jieba_index",
                            "filter": [
                                "lowercase",
                                "jieba_stop"
                            ]
                        },
                        "split_ana": {
                            "type": "pattern",
                            "pattern": self.split_parttern,
                            "lowercase": True
                        },
                        "ngram_ana": {
                            "tokenizer": "ngram_tokenizer"
                        }
                    },
                    "tokenizer": {
                        "ngram_tokenizer": {
                            "type": "ngram",
                            "min_gram": 1,
                            "max_gram": 4,
                        }
                    }
                }
            }
        }
        return res

    @property
    def _mappings(self):
        """"""
        res = {
            "mappings": {
                "properties": {
                }
            }
        }
        for k, v in self._fields.items():
            res['mappings']['properties'][k] = v.to_dict()

        return res

    def update_question(self, index, data):
        """更新数据"""
        for qa_id, insert_list in tqdm(data.items()):
            body = {'query': {'term': {'qa_id': qa_id}}}
            self.es.delete_by_query(index, body=body)
            bulk_list = []
            for dt in insert_list:
                # self.es.index(index, dt)
                bulk_list.append({'index': {}})
                bulk_list.append(dt)
            self.es.bulk(bulk_list, index=index)

    def create_question(self, index, data):
        """创建数据"""
        key_list = list(data.keys())
        for i in tqdm(range(ceil(len(key_list) / self._bulk))):
            bulk_list = []
            for qa_id in key_list[i: (i+1)*self._bulk]:
                insert_list = data[qa_id]
                for dt in insert_list:
                    bulk_list.append({'index': {}})
                    bulk_list.append(dt)
                    # self.es.index(index, dt)
            self.es.bulk(bulk_list, index=index)

    def db_to_es(self, data, index_name=None, update=True):
        """从数据库中导入"""
        index = index_name or self.index_name
        res = {}
        for dt in data:
            # dt = data[i]
            question = dt['question_standard']
            question_similar = dt['question_similar']
            mall_id = dt['mall_id']
            qa_id = dt['qa_id']
            qa_status = dt['qa_status']
            insert_data = self.body_fix({'question': question, 'ngram_question': question, 'mall_id': mall_id,
                                         'match_question': question, 'qa_id': qa_id, 'qa_status': qa_status})
            res[qa_id] = [insert_data]
            for q in question_similar.split(';'):
                res[qa_id].append(
                    self.body_fix({'question': q, 'ngram_question': q, 'match_question': q, 'qa_id': qa_id,
                                   'mall_id': mall_id, 'qa_status': qa_status})
                )
        if update:
            self.update_question(index, res)
        else:
            self.create_question(index, res)



