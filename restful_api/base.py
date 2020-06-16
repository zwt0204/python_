# -*- encoding: utf-8 -*-
"""
@File    : base.py
@Time    : 2020/6/9 10:11
@Author  : zwt
@git   : 
@Software: PyCharm
"""
from functools import wraps
from sqlalchemy.orm.query import Query
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr, as_declarative
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import AbstractConcreteBase
from contextlib import contextmanager
from sqlalchemy import inspect


engine = create_engine("mysql+pymysql://{}:{}@{}".format('root', 'password', '172.16.102.15:3306/yunshen'),
                       convert_unicode=True,
                       pool_size=1, max_overflow=0,
                       pool_recycle=100, echo=True)
Session = sessionmaker(bind=engine)


def close_session(fn):
    @wraps(fn)
    def close(obj, *args, **kwargs):
        obj.session = Session()
        res = fn(obj, *args, **kwargs)
        obj.session.close()
        return res
    return close


class RobotQuery(Query):

    @close_session
    def get(self, *args, **kwargs):
        """增加关闭的功能"""
        return super(RobotQuery, self).get(*args, **kwargs)

    @close_session
    def first(self):
        return super(RobotQuery, self).first()

    @close_session
    def all(self):
        return super(RobotQuery, self).all()


Base = declarative_base()


class RobotModel(AbstractConcreteBase, Base):
    """table映射的基类"""

    @classmethod
    def query(cls):
        """"""
        return RobotQuery(cls)

    def to_dict(self):
        return {k: getattr(self, k) for k in inspect(type(self)).c.keys()}


@contextmanager
def get_session(autocommit=False, **kwargs):
    """"""
    s = Session(autocommit=autocommit, **kwargs)
    try:
        if autocommit:
            s.begin()
        yield s
        s.commit()
    except Exception as e:
        s.rollback()
        raise e
    finally:
        s.close()


@contextmanager
def get_connect(**kwargs):

    connect = engine.connect(**kwargs)
    try:
        yield connect
    finally:
        connect.close()