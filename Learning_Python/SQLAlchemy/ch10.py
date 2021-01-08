###
# File: ch10.py
# Created Date: 2021-01-08
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday January 8th 2021 11:18:56 am
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
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

Base = automap_base()
engine = create_engine('mysql+pymysql://liuqd:liuquandong'  
                       '@localhost/liuqd', pool_recycle=3600)



# %%
Base.prepare(engine, reflect=True)


# %%
Base.classes.keys()


# %%
Cookie = Base.classes.cookies
LineItem = Base.classes.line_items


# %%
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()
for i in session.query(Cookie).limit(10):
    print(i.cookie_name,i.cookie_recipe_url)


# %%
artist = session.query(Cookie).first()
for album in artist.album_collection:
    print('{} - {}'.format(artist.Name, album.Title))

