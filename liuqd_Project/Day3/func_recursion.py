# -*- coding: utf-8 -*-
'''
Created on 2017年7月11日

@author: anddy.liu
'''
'''
def calc(n):
    print(n)
    return calc(n/2)

    


calc(10)  #这个函数携程个死循环了，Python会已知递归执行直到最大递归次数，默认就是999层
'''
def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(n/2)
    print("->",n)
    
calc(10)  #这样写就不会出现死循环了，因为上边加了条件