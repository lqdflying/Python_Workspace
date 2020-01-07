# -*- coding: utf-8 -*-
'''
Created on 2017年7月12日

@author: anddy.liu
'''
#第二类高阶函数（初级的装饰器雏形）：返回值中包含函数名（不修改函数的调用方式）
import  time

def bar():
    time.sleep(2)
    print("in the bar")

def test2(func):
    print(func)
    return func #返回值中包含函数名

#test2(bar()) #这个是把bar函数的运行结果返回给test2函数，我看上边，bar的运行结果因为没有return，所有估计运行结果是None，下边做个测试
#print(bar()) 果然返回结果是None
#test2(bar) #这个是把bar函数的内存门牌号也就是内存地址传给test2函数
#print("这里就是运行bar")
bar = test2(bar) #返回值中包含函数名，因为新的bar获得了bar函数的门牌号
bar() #但这里运行bar之前，是test2先搞完了才返回的
#print(test2(bar)) #不加小括号返回内存地址，加上小括号就能运行