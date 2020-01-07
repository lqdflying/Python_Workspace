# -*- coding: utf-8 -*-
'''
Created on 2017年7月11日

@author: anddy.liu
'''
def func1():
    '''这是个测试函数'''
    return 1

def func2():
    ''' 定义一个过程'''
    print("in the func2")
    
#函数和过程的区别在于，函数自己返回结果，结果需要再去处理，而过程自己处理结果，不需要再去处理了,过程实际上是没有返回值的函数

x = func1()
print(x)  #x接收了func1的返回值，需要额外处理才可，这里的额外处理就是print
y = func2()
print(y)  #Python中，过程也被当成是函数，过程就是没有返回值的函数，这里的返回值就是None，None就是没有返回值