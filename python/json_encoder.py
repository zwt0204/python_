# -*- encoding: utf-8 -*-
"""
@File    : json_encoder.py
@Time    : 2020/4/26 14:47
@Author  : zwt
@git   : 
@Software: PyCharm
"""
from flask.json import JSONEncoder
from datetime import datetime, date
import numpy as np


class JsonEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime) or isinstance(obj, date):
            return str(obj).replace('T', ' ')
        elif isinstance(obj, bytes):
            return obj.decode('ascii')
        elif isinstance(obj, np.ndarray):
            return list(obj)
        elif isinstance(obj, np.int64):
            return int(obj)
        else:
            return JSONEncoder.default(self, obj)


if __name__ == '__main__':
    import json
    json.dumps('', cls=JsonEncoder)