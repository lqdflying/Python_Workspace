# -*- coding: utf-8 -*-
'''
Created on 2017年7月18日

@author: anddy.liu
'''
#这段代码
def calc(n):
    return n**n
    print(calc(10))

#换成匿名函数
calc = lambda n:n**n
print(calc(10))
#匿名函数可以进行简单的数据运算

calc1 = lambda n:3 if n<4 else n

print(calc1(1))
print(calc1(5))
#匿名函数还可以进行简单的三元运算