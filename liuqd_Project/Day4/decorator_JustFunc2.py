# -*- coding: utf-8 -*-
'''
Created on 2017年7月12日

@author: anddy.liu
'''
#函数的嵌套（装饰器的另一种雏形）

x = 0
def grandpa():
    x = 1
    print(x+1)
    def dad():
        x = 2
        print(x+1)
        def son():
            x = 3
            print(x+1)
        son()
    dad()

grandpa() #实际结果是4