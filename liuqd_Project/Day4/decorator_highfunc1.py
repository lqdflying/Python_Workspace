# -*- coding: utf-8 -*-
'''
Created on 2017年7月12日

@author: anddy.liu
'''
#第一类高阶函数（初级的装饰器雏形）： 把一个函数名当做形实参传给另外一个函数（在不修改被装饰函数源代码的情况下为其添加功能）
import  time

def bar():
    time.sleep(2)
    print("in the bar")

def test1(func):
    start_time = time.time()
#     print(func)
    func() #这一句也可以运行，函数即变量，这句话就是这个含义
    stop_time = time.time()
    print("the func run time is %s" %(stop_time-start_time))

test1(bar)  #会打印函数bar()的内存地址，就是门牌号

#以上世界上实现了一个初步的装饰器的功能，就是再不修改源代码（这里的源代码是bar()）的前提下，
#为bar函数添加功能，这里添加的功能就是计算bar函数的运行时间，但是和装饰器相比，
#还有一个地方不符合就是，这里依然修改了bar函数的调用方式，也就是由bar()改为了test1(bar)
'''
func = bar 
func()  #这样也可以运行，理解函数即变量的
'''