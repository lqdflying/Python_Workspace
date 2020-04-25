# -*- coding:utf-8 -*-
###
# File: class_polymorpysim.py
# Created Date: 2020-04-24
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday April 24th 2020 10:19:04 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
class a:
    def __init__(self,name):
        self.name = name
    def record(self):
        return "the lesson from A:%s"%self.name

class b:
    def __init__(self,name):
        self.name = name
    def record(self):
        return "the lesson from B:%s"%self.name

class c:
    def __init__(self,name):
        self.name = name
    def record(self):
        return "the lesson from C:%s"%self.name

class d:
    def __init__(self,name):
        self.name = name
    def record(self):
        return "the lesson from D:%s"%self.name

def mylesson(name):
    print("mylesson is :",name.record())

anddy = a("history")
tom = b("music")
bom = c("math")
bolly = d("dance")

mylesson(anddy) #实际调用的anddy.record()
mylesson(tom) #实际调用的tom.record()
mylesson(bom) #实际调用的bom.record()
mylesson(bolly) #实际调用的bolly.record()

'''
多态性是指具有不同功能的函数可以使用相同的函数名，这样就可以用一个函数名调用不同内容的函数。
在面向对象方法中一般是这样表述多态性：向不同的对象发送同一条消息，不同的对象在接收时会产生不同的行为（即方法）。
也就是说，每个对象可以用自己的方式去响应共同的消息。所谓消息，就是调用函数，不同的行为就是指不同的实现，
即执行不同的函数。
'''

