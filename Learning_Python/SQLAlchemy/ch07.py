###
# File: ch07.py
# Created Date: 2020-12-22
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Tuesday December 22nd 2020 5:04:17 pm
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
from datetime import datetime

from sqlalchemy import Column, Integer, Numeric, String, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))
    
    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}', " \
                        "cookie_recipe_url='{self.cookie_recipe_url}', " \
                        "cookie_sku='{self.cookie_sku}', " \
                        "quantity={self.quantity}, " \
                        "unit_cost={self.unit_cost})".format(self=self)
    
class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
    
    def __repr__(self):
        return "User(username='{self.username}', " \
                     "email_address='{self.email_address}', " \
                     "phone='{self.phone}', " \
                     "password='{self.password}')".format(self=self)


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    shipped = Column(Boolean(), default=False)
    
    user =  relationship("User", backref=backref('orders', order_by=order_id))

    def __repr__(self):
        return "Order(user_id={self.user_id}, " \
                      "shipped={self.shipped})".format(self=self)

class LineItem(Base):
    __tablename__ = 'line_items'
    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))
    
    order = relationship("Order", backref=backref('line_items', order_by=line_item_id))
    cookie = relationship("Cookie", uselist=False)

    def __repr__(self):
        return "LineItems(order_id={self.order_id}, " \
                          "cookie_id={self.cookie_id}, " \
                          "quantity={self.quantity}, " \
                          "extended_cost={self.extended_cost})".format(self=self)     

# %%
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://liuqd:liuquandong'  
                       '@localhost/liuqd', pool_recycle=3600)

Session = sessionmaker(bind=engine)

session = Session()

# Base.metadata.create_all(engine)


# %%
cc_cookie = Cookie(cookie_name='chocolate chip', 
                   cookie_recipe_url='http://some.aweso.me/cookie/recipe.html', 
                   cookie_sku='CC01', 
                   quantity=12, 
                   unit_cost=0.50)


# %%
session.add(cc_cookie)


# %%
session.commit()


# %%
cc_cookie.cookie_id


# %%
dcc = Cookie(cookie_name='dark chocolate chip',
             cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
             cookie_sku='CC02',
             quantity=1,
             unit_cost=0.75)
mol = Cookie(cookie_name='molasses',
             cookie_recipe_url='http://some.aweso.me/cookie/recipe_molasses.html',
             cookie_sku='MOL01',
             quantity=1,
             unit_cost=0.80)
session.add(dcc)
session.add(mol)
session.flush()


# %%
print(dcc.cookie_id)
print(mol.cookie_id)


# %%
c1 = Cookie(cookie_name='peanut butter',
            cookie_recipe_url='http://some.aweso.me/cookie/peanut.html',
            cookie_sku='PB01',
            quantity=24,
            unit_cost=0.25)
c2 = Cookie(cookie_name='oatmeal raisin',
            cookie_recipe_url='http://some.okay.me/cookie/raisin.html',
            cookie_sku='EWW01',
            quantity=100,
            unit_cost=1.00)


# %%
session.bulk_save_objects([c1,c2])
session.commit()


# %%
c1.cookie_id


# %%
cookies = session.query(Cookie).all()
print(cookies)


# %%
for cookie in session.query(Cookie):  
    print(cookie)


# %%
print(session.query(Cookie.cookie_name, Cookie.quantity).first())


# %%
for cookie in session.query(Cookie).order_by(Cookie.quantity):
    print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))


# %%
from sqlalchemy import desc
for cookie in session.query(Cookie).order_by(desc(Cookie.quantity)):
    print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))


# %%
query = session.query(Cookie).order_by(Cookie.quantity)[:2]
print([result.cookie_name for result in query])


# %%
query = session.query(Cookie).order_by(Cookie.quantity).limit(2)
print([result.cookie_name for result in query])


# %%
from sqlalchemy import func
inv_count = session.query(func.sum(Cookie.quantity)).scalar()
print(inv_count)


# %%
rec_count = session.query(func.count(Cookie.cookie_name)).first()
print(rec_count)


# %%
rec_count = session.query(func.count(Cookie.cookie_name) \
                          .label('inventory_count')).first()
print(rec_count.keys())
print(rec_count.inventory_count)


# %%
record = session.query(Cookie).filter(Cookie.cookie_name == 'chocolate chip').first()
print(record)


# %%
record = session.query(Cookie).filter_by(cookie_name='chocolate chip').first()
print(record)


# %%
query = session.query(Cookie).filter(Cookie.cookie_name.like('%chocolate%'))
for record in query:                       
    print(record.cookie_name)


# %%
results = session.query(Cookie.cookie_name, 'SKU-' + Cookie.cookie_sku).all()
for row in results:
    print(row)


# %%
from sqlalchemy import cast
query = session.query(Cookie.cookie_name,
                      cast((Cookie.quantity * Cookie.unit_cost), 
                           Numeric(12,2)).label('inv_cost'))
for result in query:
    print('{} - {}'.format(result.cookie_name, result.inv_cost))


# %%
from sqlalchemy import and_, or_, not_
query = session.query(Cookie).filter(
    Cookie.quantity > 23,
    Cookie.unit_cost < 0.40
)
for result in query:
    print(result.cookie_name)


# %%
from sqlalchemy import and_, or_, not_
query = session.query(Cookie).filter(
    or_(
        Cookie.quantity.between(10, 50),
        Cookie.cookie_name.contains('chip')
    )
)
for result in query:
    print(result.cookie_name)


# %%
query = session.query(Cookie)
cc_cookie = query.filter(Cookie.cookie_name == "chocolate chip").first()
cc_cookie.quantity = cc_cookie.quantity + 120
session.commit()
print(cc_cookie.quantity)


# %%
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "chocolate chip")
query.update({Cookie.quantity: Cookie.quantity - 20})

cc_cookie = query.first()
print(cc_cookie.quantity)


# %%
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "dark chocolate chip")
dcc_cookie = query.one()
session.delete(dcc_cookie)
session.commit()
dcc_cookie = query.first()
print(dcc_cookie)


# %%
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "molasses")
query.delete()
mol_cookie = query.first()
print(mol_cookie)


# %%
cookiemon = User(username='cookiemon', 
                 email_address='mon@cookie.com', 
                 phone='111-111-1111', 
                 password='password')
cakeeater = User(username='cakeeater', 
                 email_address='cakeeater@cake.com', 
                 phone='222-222-2222', 
                 password='password')
pieperson = User(username='pieperson', 
                 email_address='person@pie.com', 
                 phone='333-333-3333', 
                 password='password')
session.add(cookiemon)
session.add(cakeeater)
session.add(pieperson)
session.commit()


# %%
o1 = Order()
o1.user = cookiemon
session.add(o1)

cc = session.query(Cookie).filter(Cookie.cookie_name == 
                                  "chocolate chip").one()
line1 = LineItem(cookie=cc, quantity=2, extended_cost=1.00)

pb = session.query(Cookie).filter(Cookie.cookie_name == 
                                  "peanut butter").one()
line2 = LineItem(quantity=12, extended_cost=3.00)
line2.cookie = pb 
line2.order = o1

o1.line_items.append(line1)
o1.line_items.append(line2)
session.commit()


# %%
o2 = Order()
o2.user = cakeeater

cc = session.query(Cookie).filter(Cookie.cookie_name == 
                                  "chocolate chip").one()
line1 = LineItem(cookie=cc, quantity=24, extended_cost=12.00)

oat = session.query(Cookie).filter(Cookie.cookie_name == 
                                   "oatmeal raisin").one()
line2 = LineItem(cookie=oat, quantity=6, extended_cost=6.00)

o2.line_items.append(line1)
o2.line_items.append(line2)

session.add(o2)
session.commit()


# %%
query = session.query(Order.order_id, User.username, User.phone,
                      Cookie.cookie_name, LineItem.quantity,
                      LineItem.extended_cost)
query = query.join(User).join(LineItem).join(Cookie)
results = query.filter(User.username == 'cookiemon').all()
print(results)


# %%
query = session.query(User.username, func.count(Order.order_id))
query = query.outerjoin(Order).group_by(User.username)
for row in query:
    print(row)


# %%
class Employee(Base):
    __tablename__ = 'employees'
    
    id = Column(Integer(), primary_key=True)
    manager_id = Column(Integer(), ForeignKey('employees.id'))
    name = Column(String(255), nullable=False)
    
    manager = relationship("Employee", backref=backref('reports'), remote_side=[id])

Base.metadata.create_all(engine)


# %%
marsha = Employee(name='Marsha')
fred = Employee(name='Fred')
marsha.reports.append(fred)
session.add(marsha)
session.commit()


# %%
for report in marsha.reports:
    print(report.name)


# %%
query = session.query(User.username, func.count(Order.order_id))
query = query.outerjoin(Order).group_by(User.username)
for row in query:
    print(row)


# %%
def get_orders_by_customer(cust_name):
    query = session.query(Order.order_id, User.username, User.phone,
                      Cookie.cookie_name, LineItem.quantity,
                      LineItem.extended_cost)
    query = query.join(User).join(LineItem).join(Cookie)
    results = query.filter(User.username == cust_name).all()
    return results

get_orders_by_customer('cakeeater')


# %%
def get_orders_by_customer(cust_name, shipped=None, details=False):
    query = session.query(Order.order_id, User.username, User.phone)
    query = query.join(User)
    if details:
        query = query.add_columns(Cookie.cookie_name, LineItem.quantity,
                          LineItem.extended_cost)
        query = query.join(LineItem).join(Cookie)
    if shipped is not None:
        query = query.filter(Order.shipped == shipped)
    results = query.filter(User.username == cust_name).all()
    return results

print(get_orders_by_customer('cakeeater'))

print(get_orders_by_customer('cakeeater', details=True))

print(get_orders_by_customer('cakeeater', shipped=True))

print(get_orders_by_customer('cakeeater', shipped=False))

print(get_orders_by_customer('cakeeater', shipped=False, details=True))


# %%
from sqlalchemy import text
query = session.query(User).filter(text("username='cookiemon'"))
print(query.all())


