###
# File: Association Proxy - Test.py
# Created Date: 2021-01-08
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday January 9th 2021 12:24:36 pm
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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://liuqd:liuquandong'  
                       '@localhost/liuqd', pool_recycle=3600, echo=False)

Session = sessionmaker(bind=engine)


# %%
from datetime import datetime

from sqlalchemy import Column, Integer, Numeric, String, Table, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy


Base = declarative_base()


class Ingredient(Base):
    __tablename__ = 'ingredients'
    
    ingredient_id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)
    
    def __init__(self, name):
        self.name = name
        
    
    def __repr__(self):
        return "Ingredient(name='{self.name}')".format(self=self)


class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    
    # ingredients = relationship("Ingredient", secondary='cookieingredients_table')
    
    ingredient_names = association_proxy('ingredients', 'name')
        
    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}'".format(self=self)

class cookieingredients_table(Base):
    __tablename__ = 'cookieingredients'

    cookie_id = Column(Integer(), ForeignKey("cookies.cookie_id"), primary_key=True)
    ingredient_id = Column(Integer(), ForeignKey("ingredients.ingredient_id"), primary_key=True)

Base.metadata.create_all(engine)


# %%
session = Session()
cc_cookie = Cookie(cookie_name='chocolate chip')
dcc = Cookie(cookie_name='dark chocolate chip')

flour = Ingredient(name='Flour')
sugar = Ingredient(name='Sugar')
egg = Ingredient(name='Egg')
cc = Ingredient(name='Chocolate Chips')


session.add_all([cc_cookie, dcc])
session.add_all([flour,sugar,egg,cc])


session.add_all([
    cookieingredients_table(cookie_id=session.query(Cookie.cookie_id).filter(Cookie.cookie_name=='chocolate chip'), \
                            ingredient_id=session.query(Ingredient.ingredient_id).filter(Ingredient.name=='Flour')),
    cookieingredients_table(cookie_id=session.query(Cookie.cookie_id).filter(Cookie.cookie_name=='chocolate chip'), \
                            ingredient_id=session.query(Ingredient.ingredient_id).filter(Ingredient.name=='Egg')),
    cookieingredients_table(cookie_id=session.query(Cookie.cookie_id).filter(Cookie.cookie_name=='dark chocolate chip'), \
                            ingredient_id=session.query(Ingredient.ingredient_id).filter(Ingredient.name=='Egg'))
])

# %%
cc_cookie.ingredients.extend([flour, sugar, egg, cc])
session.add(cc_cookie)
session.add(dcc)
session.bulk_save_objects([flour, sugar, egg, cc])
session.flush()


# %%
[ingredient.name for ingredient in cc_cookie.ingredients]


# %%
cc_cookie.ingredient_names


# %%
cc_cookie.ingredient_names.append('Oil')
session.flush()


# %%
cc_cookie.ingredient_names


# %%
cc_cookie.ingredients


# %%
dcc_ingredient_list = ['Flour', 'Sugar', 'Egg', 'Dark Chocolate Chips', 'Oil']


# %%
existing_ingredients = session.query(Ingredient).filter(
    Ingredient.name.in_(dcc_ingredient_list)).all()


# %%
missing = set(dcc_ingredient_list) - set([x.name for x in 
                                          existing_ingredients])


# %%
missing


# %%
dcc.ingredients.extend(existing_ingredients)


# %%
dcc.ingredient_names.extend(list(missing))


# %%
dcc.ingredient_names


