# -*- coding:utf-8 -*-
###
# File: class_example.py
# Created Date: 2020-04-19
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday April 19th 2020 10:25:05 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

class MyClass:
   """一个简单的类实例"""
   i = "不变的独立类属性" #这就是一个独立类属性
   def __init__(self,name):
      self.name = name #定义一个实例属性
   def f(self):
       return 'hello world:%s'%self.name
# 实例化类,生成两个实例对象
x = MyClass("liu")
y = MyClass("anddy")
#we created an object by adding parentheses to the name of the class. We then assigned that new instance to the variable cool_instancefor safe-keeping.
#类名MyClass后边加括号是真实的在内存中实例化一个类的操作,赋值给前边的x变量是为了safe-keeping(保证后边可以引用这个实例化类)
# 访问类的属性和方法
print("实例对象x的类的属性 i 为：", x.i)
print("实例对象y的类的属性 i 为：", y.i)
print("获取类MyClass的类属性的正确方法：", MyClass.i)
print("实例对象x的的方法 f 输出为：", x.f())
print("实例对象y的的方法 f 输出为：", y.f())

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
print(x.r, x.i)

class circle1:
    pi = 3.14
    def __init__(self,diameter,myname):
        print("New circle1 with diameter:  {diameter}".format(diameter = diameter))
#由于构造函数里有print动作,所以下边的类的实例化操作会触发动作,进而导致print的输出
teaching_table1 = circle1(36, "liuqd")
#print(teaching_table1.diameter) 
#上边这个print会报错:'circle1' object has no attribute 'diameter'
class circle2:
    pi = 3.14
    def __init__(self,diameter,myname):
        self.diameter = diameter
        self.myname = myname
        print("New circle2 with diameter:  {diameter}".format(diameter = diameter))

teaching_table2 = circle2(36, "liuqd")
print(teaching_table2.diameter)

class Employee:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
argus = Employee("Argus Filch")
print(argus)