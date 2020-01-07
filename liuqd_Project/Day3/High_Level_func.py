# -*- coding: utf-8 -*-
'''
Created on 2017年7月12日

@author: anddy.liu
'''

#第一行中高阶函数的形式：把一个函数名当做形实参传给另外一个函数
# def add(a,b,f): #变量指向函数，这个def出来的add就是一个高阶函数
#     return f(a)+f(b)
# 
# res = add(2,-4,abs)
# 
# print(res)

def bar():
    print("in the bar")

def test1(func):
    print(func)
    func() #这一句也可以运行，函数即变量，这句话就是这个含义

test1(bar)  #会打印函数bar()的内存地址，就是门牌号

func = bar 
func()  #这样也可以运行，理解函数即变量的含义