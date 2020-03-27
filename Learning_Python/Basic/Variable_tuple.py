# -*- coding: utf-8 -*-
'''
Created on 2017年8月11日

@author: anddy.liu
'''
tuple_1 = ("liu","q","d")
tuple_2 = ("liu")
tuple_3 = ("liu",)
print("元组的类型以及访问".center(40,"+"))
print(type(tuple_1),tuple_1[1:3])
print(type(tuple_2),tuple_2)
print(type(tuple_3),tuple_3)
tuple_4 = tuple_1 + tuple_3
print("元组的拼接",tuple_4)
del tuple_3
#print("删除后的元组再访问会有异常",tuple_3)