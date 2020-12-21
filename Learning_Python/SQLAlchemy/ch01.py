###
# File: ch01.py
# Created Date: 2020-12-21
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Monday December 21st 2020 4:28:18 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from sqlalchemy import MetaData
metadata = MetaData()

# %%
from datetime import datetime


# %%
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, DateTime, Boolean


# %%
from sqlalchemy import create_engine


# %%
# engine = create_engine('sqlite:///:memory:')
engine = create_engine('mysql+pymysql://liuqd:liuquandong'  
                       '@localhost/liuqd', pool_recycle=3600)


# %%
cookies = Table('cookies', metadata,
    Column('cookie_id', Integer(), primary_key=True),
    Column('cookie_name', String(50), index=True),
    Column('cookie_recipe_url', String(255)),
    Column('cookie_sku', String(55)),
    Column('quantity', Integer()),
    Column('unit_cost', Numeric(12, 2))
)


# %%
users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)


# %%
orders = Table('orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id')),
    Column('shipped', Boolean(), default=False)
)

line_items = Table('line_items', metadata,
    Column('line_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),
    Column('cookie_id', ForeignKey('cookies.cookie_id')),
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12, 2))
)


# %%
metadata.create_all(engine)


