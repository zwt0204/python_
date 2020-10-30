#!/user/bin/env python
# coding=utf-8
"""
@file: utils.py
@author: zwt
@time: 2020/10/30 16:34
@desc: 
"""
from flask.json import JSONEncoder
from datetime import datetime, date
import numpy as np


class DataEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime) or isinstance(obj, date):
            return str(obj).replace('T', ' ')
        elif isinstance(obj, bytes):
            return str(obj)
        elif isinstance(obj, np.ndarray):
            return list(obj)
        elif isinstance(obj, np.int64):
            return int(obj)
        else:
            return JSONEncoder.default(self, obj)