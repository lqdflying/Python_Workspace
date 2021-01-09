###
# File: Association Proxy - Test-v1.py
# Created Date: 2021-01-09
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday January 9th 2021 12:40:46 pm
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
class Department(Base):
   __tablename__ = 'department'
   id = Column(Integer(), primary_key = True)
   name = Column(String(50))
   employees = relationship('Employee', secondary = 'link')
   
class Employee(Base):
   __tablename__ = 'employee'
   id = Column(Integer(), primary_key = True)
   name = Column(String(50))
   departments = relationship('Department',secondary='link')

class Link(Base):
    __tablename__ = 'link'
    department_id = Column(
        Integer, 
        ForeignKey('department.id'), 
        primary_key = True)

    employee_id = Column(
        Integer, 
        ForeignKey('employee.id'), 
        primary_key = True)

Base.metadata.create_all(engine)
# %%
d1 = Department(name = "Accounts")
d2 = Department(name = "Sales")
d3 = Department(name = "Marketing")

e1 = Employee(name = "John")
e2 = Employee(name = "Tony")
e3 = Employee(name = "Graham")

# %%
e1.departments.append(d1)
e2.departments.append(d3)
d1.employees.append(e3)
d2.employees.append(e2)
d3.employees.append(e1)
e3.departments.append(d2)

# %%
ss.add(e1)
ss.add(e2)
ss.add(d1)
ss.add(d2)
ss.add(d3)
ss.add(e3)
ss.commit()

# %%
