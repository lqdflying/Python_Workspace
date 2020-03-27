# -*- coding: utf-8 -*-
'''
Created on 2017年7月12日

@author: anddy.liu
'''

    
def foo():
    print("in the foo")
    bar()

def bar():
    print("in the bar") #在foo下边定义bar也能运行，但没关系，只要foo()执行是在这两个的后边就行

foo()