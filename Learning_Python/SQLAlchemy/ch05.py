###
# File: ch05.py
# Created Date: 2020-12-31
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Thursday January 7th 2021 5:56:40 pm
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
from sqlalchemy import MetaData, Table, create_engine
metadata = MetaData()
engine = create_engine('mysql+pymysql://liuqd:liuquandong'  
                       '@localhost/liuqd', pool_recycle=3600)

engine.pool.status()

# %%
connection = engine.connect()
# %%
cookies = Table('cookies', metadata, autoload=True, autoload_with=engine)


# %%
line_items = Table('line_items', metadata, autoload=True, autoload_with=engine)


# %%
cookies.columns.keys()


# %%
from sqlalchemy import select
s = select([cookies]).limit(10)
connection.execute(s).fetchall()


# %%
cookies.foreign_keys
line_items.foreign_keys


# %%
from sqlalchemy import ForeignKeyConstraint
album.append_constraint(
    ForeignKeyConstraint(['ArtistId'], ['artist.ArtistId'])
)


# %%
metadata.tables['line_items']


# %%
str(artist.join(album))


# %%
metadata.reflect(bind=engine)
metadata.tables.keys()

# %%
metadata.tables.keys()


# %%
users = metadata.tables['users']


# %%
from sqlalchemy import select
s = select([users]).limit(10)
engine.execute(s).fetchall()





# %%
