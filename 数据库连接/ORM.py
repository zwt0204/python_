# -*- encoding: utf-8 -*-
"""
@File    : ORM.py
@Time    : 2020/6/16 16:46
@Author  : zwt
@git   : 
@Software: PyCharm
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# 连接数据库
engine = create_engine("mysql+pymysql://{}:{}@{}".format('root', '123456', '127.0.0.1:3306/test'),
                       echo=True)  # echo=True表示打印出相关的sql语句
# 声明性基类
Base = declarative_base()


class User(Base):
    # 表名
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


if __name__ == '__main__':
    # 创建表
    # Base.metadata.create_all(engine)
    ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(ed_user)
    session.commit()
    our_user = session.query(User).filter_by(name='ed').first()
    print(our_user)