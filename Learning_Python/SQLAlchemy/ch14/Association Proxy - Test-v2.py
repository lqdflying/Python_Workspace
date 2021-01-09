###
# File: Association Proxy - Test-v2.py
# Created Date: 2021-01-09
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday January 9th 2021 12:40:59 pm
# 
# Copyright (c) 2021 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###


# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %%
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://liuqd:liuquandong'  
                       '@localhost/liuqd', pool_recycle=3600, echo=True)
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
ss = Session()
Base = declarative_base()

# %%
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    # association proxy of "user_keywords" collection
    # to "keyword" attribute
    keywords = association_proxy('user_keywords', 'keyword') # 中间表和Many2Many表的名字

    def __init__(self, name):
        self.name = name

class Keyword(Base):
    __tablename__ = 'keyword'
    id = Column(Integer, primary_key=True)
    keyword = Column('keyword', String(64)) # 要加跟表名一样的标签

    def __init__(self, keyword):
        self.keyword = keyword

    def __repr__(self):
        return 'Keyword(%s)' % repr(self.keyword)

class UserKeyword(Base):
    __tablename__ = 'user_keyword'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    keyword_id = Column(Integer, ForeignKey('keyword.id'), primary_key=True)
    special_key = Column(String(50))

    # bidirectional attribute/collection of "user"/"user_keywords"
    user = relationship(User,
                backref=backref("user_keywords",
                                cascade="all, delete-orphan")
            )

    # reference to the "Keyword" object
    keyword = relationship("Keyword")

    def __init__(self, keyword=None, user=None, special_key=None):
        self.user = user
        self.keyword = keyword
        self.special_key = special_key
    def __repr__(self):
        return f'User({self.user_id})-Keyword({self.keyword_id })_self.special_key '

Base.metadata.create_all(engine)
# %%
ss.add_all([
    Keyword('shadow'), Keyword('LOR1'), Keyword('WWII'),
    User('Kevin'), User('Olivia'),
])
ss.add_all([
    UserKeyword(user=ss.query(User).get(1), keyword=ss.query(Keyword).get(3), special_key ='abc'),
    UserKeyword(user=ss.query(User).get(2), keyword=ss.query(Keyword).get(3), special_key ='efg'),
    UserKeyword(user=ss.query(User).get(2), keyword=ss.query(Keyword).get(2), special_key ='cde'),
])
# %%
ss.commit()
# %%
