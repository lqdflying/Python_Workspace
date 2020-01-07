# -*- coding: utf-8 -*-
'''
Created on 2017年7月13日

@author: anddy.liu
'''
def test(func):
    name = input("enter a name:")
    def inner(*agrs,**kwargs):
        func(*agrs,**kwargs)
        print("内部调用完毕,同时输出一个值%s"%(name))
    return inner  #这里的inner就是个壳

def home():
    print("原home函数会输出一个home")

home = test(home)

home()