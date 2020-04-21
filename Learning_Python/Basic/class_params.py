# -*- coding:utf-8 -*-
###
# File: class_params.py
# Created Date: 2020-04-20
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Tuesday April 21st 2020 4:12:01 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
class People(object):
    # 类变量可以由所有的对象访问，但是对象只能访问，不可修改
    # 用来做资源共享
    total = 0 #这里就是定义了一个类变量
    __in = "in params"
    # 初始化函数，添加对象属性
    def __init__(self,name,age,school):
        # 给对象属性赋值
        self.name = name #实例变量1
        self.age = age #实例变量2
        self.school = school #实例变量3
        # 只能使用类修改类变量的值
        People.total += 1
    def func(self):
        print("打印实例属性: ", self.name)
    def get_private(self):
        return "私有属性:%s"%self.__in
p = People('liu',33,'USA') #实例化一个类
print("打印实例属性: ",p.name)
print("打印类属性: ",p.total)
p.total = 50 #错误的修改类属性
print("打印类属性,发现根本没修改,证明通过操作实例不能修改类属性: ",p.total)
People.total = 100 #正确的修改类属性
print("打印类属性,发现已被修改: ",p.total)
print("实例属性修改前:".center(30,'+'))
p.func()
p.name = "quan" #修改实例属性,看看调用方法会
print("实例属性修改后:".center(30,'+'))
p.func()
print("p这个实例所有可用的属性和方法可以使用dir找出:\n",dir(p))
People.total = 0
# p1和p2是两个不同的对象，这两个对象各自的信息不共享,但是类变量是共享的并且可传递
p1 = People('雷军',21,'小米大学')
print (People.total) #类变量+1
p1 = People('马化腾',22,'腾讯大学')
print (People.total) #类变量再加1,因为右上边的类定义,导致了类变量的改变,这里再次改变
# print (People.name) #类无法访问对象实例的属性,这个print会报错
print (p1.total) #对象实例可以访问类属性/类变量
# 给对象p1添加了一个total属性
p1.total = 100 #对象没有办法修改类变量的值,但是可以给实例添加一个和类变量同名的变量
print (p1.total)
print ("类的变量的值不会被修改:\n",People.total) 
People.total = 1000 # 如果需要修改类变量的值，只能由类调用修改
print ("类变量的值，只能由类调用修改:\n",People.total)
# 对象访问到的是修改之后的值
print ("这里输出的不是类变量,是外部定义的实例变量:\n",p1.total)

p3 = People('张三',23,'清华')
# 获取对象的属性值，如果属性不存在，会出现异常
# AttributeError: 'People' object has no attribute  'ssss'
# name = p3.ssss
# print (name)
# 使用getattr(object,name,default)函数,会把获取到的属性值返回
# object 要获取属性的对象 name 要获取的属性名  default  当属性不存在，赋一个默认值
# 如果属性不存在，可以给一个默认值，不会让程序出现异常
age = getattr(p3,'just',"go")
print ("不会报错,因为使用getattr为不存在的属性赋值了默认值:\n",age)
# hasattr(object,name) 判断某个对象是否拥有某个属性
# 判断会返回结果，如果有这个属性返回Ture，没有返回False
s = hasattr(p3,'age')
print (s)
# 先判断是否有这个属性，在执行获取属性值得操作
if hasattr(p3,'ssss'):
    s = p3.ssss
else:
    print ('p3没有ssss这个属性')

print("正确的调用私有属性:", p3.get_private())
print("错误的调用私有属性:", p3.__in)