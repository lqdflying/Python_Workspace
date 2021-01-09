

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://liuqd:liuquandong'  
                       '@localhost/liuqd', pool_recycle=3600, echo=True)

Session = sessionmaker(bind=engine)


# %%
from datetime import datetime

from sqlalchemy import Column, Integer, Numeric, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.associationproxy import association_proxy


Base = declarative_base()


cookieingredients_table = Table('cookieingredients', Base.metadata,
    Column('cookie_id', Integer, ForeignKey("cookies.cookie_id"),
           primary_key=True),
    Column('ingredient_id', Integer, ForeignKey("ingredients.ingredient_id"),
           primary_key=True)
)


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
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))
    
    ingredients = relationship("Ingredient", secondary=lambda: cookieingredients_table)
    
    ingredient_names = association_proxy('ingredients', 'name')

        
    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}', " \
                       "cookie_recipe_url='{self.cookie_recipe_url}', " \
                       "cookie_sku='{self.cookie_sku}', " \
                       "quantity={self.quantity}, " \
                       "unit_cost={self.unit_cost})".format(self=self)

Base.metadata.create_all(engine)


# %%
session = Session()
cc_cookie = Cookie(cookie_name='chocolate chip', 
                   cookie_recipe_url='http://some.aweso.me/cookie/recipe.html', 
                   cookie_sku='CC01', 
                   quantity=12, 
                   unit_cost=0.50)
dcc = Cookie(cookie_name='dark chocolate chip',
             cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
             cookie_sku='CC02',
             quantity=1,
             unit_cost=0.75)

flour = Ingredient(name='Flour')
sugar = Ingredient(name='Sugar')
egg = Ingredient(name='Egg')
cc = Ingredient(name='Chocolate Chips')

cc_cookie.ingredients.extend([flour, sugar, egg, cc])
session.add(cc_cookie)
session.add(dcc)
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


