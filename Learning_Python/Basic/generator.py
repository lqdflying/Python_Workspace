# -*- coding: utf-8 -*-
'''
Created on 2017年11月1日

@author: anddy.liu
'''
def gensquares(N):
    for i in range(N):
        yield i ** 2 #函数里使用yield就变成了生成器
print("第一种打印方式".center(30,"+"))
var = gensquares(5)
print(next(var))
print(next(var))
print(next(var))
print("第二种打印方式".center(30,"+"))
for item in gensquares(5):
    print(item)
print("下边证明，yield不仅能return值，还能receive从外边传过来的值".center(30,"+"))
def receivedata():
    c = yield
    print("gogogo",c)

d = receivedata()
d.__next__() #这里得执行一次，只有执行一次，receivedata才会变成生成器，并在该中断的地方中断，不然receivedata就是个函数
while True:
    try:
        d.send(2)
    except StopIteration:
        print("程序结束")
        break