# -*- coding:utf-8 -*-
###
# File: generator.py
# Created Date: 2020-05-27
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 27th 2020 9:07:01 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

def gensquares(N):
    for i in range(N):
        yield i ** 2 #函数里使用yield就变成了生成器
print("第一种打印方式".center(30,"+"))
var = gensquares(5)
print(next(var))
print(next(var))
print(next(var))

print("第二种打印方式".center(30,"+"))
for item in gensquares(5):
    print(item)


print("下边证明，yield不仅能return值，还能receive从外边传过来的值".center(30,"+"))
def receivedata():
    c = yield
    print("gogogo",c)

d = receivedata()
d.__next__() #这里得执行一次，只有执行一次，receivedata才会变成生成器，并在该中断的地方中断，不然receivedata就是个函数
while True:
    try:
        d.send(2) #生成器的send()就是用来传递参数给yield用的
    except StopIteration:
        print("程序结束")
        break

print("send()和__next__的区别".center(30,"+"))

def test():
    print("generator start")
    n = 1
    while True:
        
        yield_expression_value = yield n
        print("yield_expression_value = %s" %(yield_expression_value))
        
        # yield n
        n += 1


#创建generator对象
generator = test()
# print(type(generator))

#启动generator
# print("生成器调用__next__()返回的是yield声明的变量的值: %d" %generator.__next__())
print("生成器初始化:调用send(None)返回的是yield声明的变量的初始值: %d" %generator.send(None))
# 这里如果想用send()的方式初始化,则只能send(None),否则报错
# can't send non-None value to a just-started generator

print("第二次调用__next__()之前,会执行一次test函数里的print语句,当然__next__()永远只会返回yield的值: %d" %generator.__next__())
#发送值给yield表达式,虽然是发送了个None
#这一句执行后,test()函数里的print语句就会执行

print("使用send()后,不必须需要使用__next__,生成器会自动返回下一个yield的值: %d" %generator.send(66))
#发送值给yield表达式,发送的是66
#这一句执行后,test()函数里的print语句就会执行

