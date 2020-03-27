# -*- coding: utf-8 -*-
'''
Created on 2017年7月8日

@author: anddy.liu
'''
names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei"] #replace方法只能处理字符串，不能处理数组
name = "LiuQuandong"

#print(name.replace("Q",1))  #这样写就会报错，看来replace必须是同类型数据替换，1不加引号代表是int,加了引号才代表是str
print(name.replace("u","1"))
print(name.replace("u","1",1)) #只替换找到的第一个

print(name.rfind("u"))

print(name.find("u"))
#如果有多个重复的字符的时候才有效果，rfind是找右边的第一个的index，find是找左边的第一个的index

print(name.rfind("L"))

print(name.find("L"))