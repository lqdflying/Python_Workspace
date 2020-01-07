# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import shelve
d = shelve.open('shelve_test') #打开一个文件
print(d.get("name"))
print(d.get("date"))