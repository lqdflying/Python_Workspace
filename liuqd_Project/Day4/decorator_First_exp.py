# -*- coding: utf-8 -*-
'''
Created on 2017年7月12日

@author: anddy.liu
'''
import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print("the func run time is %s"%(stop_time-start_time))
    return warpper
#    return warpper() #这样写是会报错的

#在定义装饰器函数warpper时，返回值应该是包装的函数对象，而不是包装的函数调用。应该写为“return warpper”，而不是“return warpper()”

@timmer

def test1():
    time.sleep(3)
    print("in the test1")

test1()

#timmer(func)