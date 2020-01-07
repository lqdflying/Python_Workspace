# -*- coding: utf-8 -*-
'''
Created on 2018年3月11日

@author: anddy.liu
'''
import shelve
import datetime
print('创造数据'.center(30,"+"))
d = shelve.open('shelve_test',flag='c') #打开一个文件
'''
    Optional argument *flag* can be 'r' for read-only access, 'w'
    for read-write access of an existing database, 'c' (default)for read-write access
    to a new or existing database, and 'n' for read-write access to a new
    database.

    Note: 'r' and 'w' fail if the database doesn't exist; 'c' creates it
    only if it doesn't exist; and 'n' always creates a new database.
'''

info = {"age":22,"job":"IT"}


name = ["alex","rain","test"]
d[liuqdteste"] = name #持久化列表
d["info"] = name #持久化字典
d["date"] = datetime.datetime.now() #持久化time格式

d.close()

#这个脚本执行完了以后会多三个文件：shelve_test.bak、shelve_test.dat、shelve_test.dir

print('读取数据'.center(30,"+"))
d = shelve.open('shelve_test') #打开一个文件
print(d.get("name"))
print(d.get("date"))
d.close()

print('修改数据之错误的方法'.center(30,"+"))
d = shelve.open('shelve_test',flag='w') #打开一个文件
d["name"].append('gpgpg')
print('会发现数据并么有会写，还是旧的：\n',d['name'])
d.close()

print('修改数据之正确的方法1'.center(30,"+"))
d = shelve.open('shelve_test',flag='w') #打开一个文件
data=d['name']
data.append('gpgpg')
d["name"]=data
print('只有传值给一个变量，才回向赋值，数据才是新的：\n',d['name'])
d.close()

print('修改数据之正确的方法2'.center(30,"+"))
d = shelve.open('shelve_test',flag='w',writeback=True) #打开一个文件
d["name"].append('liuqd')
print('writeback设置为true，也可以做到数据修改后自动会写，数据才是新的：\n',d['name'])
d.close()