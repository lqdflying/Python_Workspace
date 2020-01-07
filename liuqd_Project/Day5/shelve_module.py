# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import shelve
import datetime
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
d["name"] = name #持久化列表
d["info"] = name #持久化字典
d["date"] = datetime.datetime.now() #持久化time格式

d.close()

#这个脚本执行完了以后会多三个文件：shelve_test.bak、shelve_test.dat、shelve_test.dir