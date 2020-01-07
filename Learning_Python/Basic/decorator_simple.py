# -*- coding: utf-8 -*-
'''
Created on 2017年11月1日

@author: anddy.liu
'''
def use_logging(func):
    def wrapper(*args, **kwargs):
        print("[The function]:%s is running" % func.__name__)
        return func(*args)
    return wrapper

@use_logging
def foo():
    print("i am foo")

@use_logging
def bar():
    print("i am bar")

bar()