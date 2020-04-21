# -*- coding:utf-8 -*-
###
# File: class_method.py
# Created Date: 2020-04-21
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Tuesday April 21st 2020 10:53:57 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
class class_sample:
    @staticmethod
    def fun():
        print('静态方法')

    @classmethod
    def a(cls):
        print('类方法')

    # 普通方法
    def b(self):
        print('普通方法')

#静态方法和类方法都可以直接使用类名调用
class_sample.fun()
class_sample.a()

C = class_sample()
#所有的方法实例化后都可以被实例对象拿来调用
C.fun()
C.a()
C.b()


class Site:
    def __init__(self, name, url):
        self.name = name       # public
        self.__url = url   # private
    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)
    def __foo(self):          # 私有方法
        print('这是私有方法')
    def foo(self):            # 公共方法
        print('这是公共方法')
        self.__foo()
x = Site('anddy', 'www.anddy.com')
x.who()        # 正常输出
x.foo()        # 正常输出,公有方法里可以引用私有方法
#x.__foo()      # 报错

class Employee():
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"

class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return '这个人的名字是%s,已经有%d岁了！'%(self.name,self.age)

    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))

a = people('孙悟空',999)
print(a)
a.speak()