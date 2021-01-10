# -*- coding: utf-8 -*-
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String,DateTime,Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import sessionmaker

# 实例一个引擎
dburl = "mysql+pymysql://testuser:testpass@127.0.0.1:3358/testdb?charset=utf8"
engine = create_engine(dburl, echo=True, encoding="utf-8")
Base = declarative_base()
class User_table(Base):
    __tablename__ = 'userinfo'
    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String(50), index=True)
    age = Column(Integer())
    birthday = Column(Date(), nullable=False)
    sex = Column(String(10))
    education = Column(String(50))
    create_time = Column(DateTime(), default=datetime.now)
    update_time = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return (f"{self.user_id}, {self.user_name}, {self.age}, {self.birthday}, "
                f"{self.sex}, {self.education}, {self.education}, "
                f"{self.create_time}, {self.update_time}")

try:
    Base.metadata.create_all(engine)
except Exception as e:
    print("create error {e}")

# 创建session
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
user_add1 = User_table(
        user_name="anger",
        age=2,
        birthday="2018-01-01",
        sex="man",
        education="n")

user_add2 = User_table(
        user_name="em",
        age=30,
        birthday="1990-01-01",
        sex="wman",
        education="e")

user_add3 = User_table(
        user_name="gold",
        age=10,
        birthday="2010-01-01",
        sex="man",
        education="m")
session.add(user_add1)
session.add(user_add2)
session.add(user_add3)
#查询
for result in session.query(User_table):
    print(result)
session.commit()

