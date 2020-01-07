# -*- coding: utf-8 -*-
'''
Created on 2017年7月7日

@author: anddy.liu
'''
import copy

person = ["name",["父亲","母亲",100]]

'''
#讲三种浅copy方式
p1 = copy.copy(person)

p2 = person[:]

p3 = list(person)

print("first copy:",p1)
print("secondary copy:",p2)
print("third copy:",p3)
'''

#浅copy是有用的，用来创建联合账号
p1 = copy.copy(person)
p2 = person[:]

p1[0] = "liuquandong"
p2[0] = "chengwenxia"

print("一起给父母存的当前养老款:",p1)
print("一起给父母存的当前养老款:",p2)
p1[1][2] = 50  #存款减少为50

print("修正后的养老款:",p1)
print("修正后的养老款:",p2)

