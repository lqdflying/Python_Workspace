# -*- coding:utf-8 -*-
###
# File: yield_and_from.py
# Created Date: 2020-05-24
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Monday May 25th 2020 11:11:16 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

#yield和yield from 是不一样的
def coroutine_example(name):
    print('start coroutine...name:', name)

    while True:
        x = yield name #调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
        if x is None:
            return f'\tcoroutine_example()函数整个结束后的返回值[\n\t\t\t{x}\n\t\t]'
        print('send值:', x)

def coroutine_from(father):
    result = yield from coroutine_example(father)
    return f"coroutine_from()的返回值[\n\t{result}\n\t]"

coro = coroutine_from('liu')
coro.__next__()
try:
    coro.send(None)
except StopIteration as e:
    print('try-except返回值[\n\t{}\n]'.format(e.value))

def fab(max):
     n,a,b = 0,0,1
     while n < max:
          yield b
          # print b
          a, b = b, a + b
          n = n + 1
f=fab(5)
'''
f.__next__()
print(f.__next__()) #1
print(f.__next__()) #2
print(f.__next__()) #3
print(f.__next__()) #5
# print(f.__next__()) #StopIteration
'''
for i in f:
    print(i) #针对生成器使用for调用也能自动的处理StopIteration异常

'''
def f_wrapper(fun_iterable):
    print('start')
    for item  in fun_iterable:
        yield item
    print('end')

wrap = f_wrapper(fab(5))
for i in wrap:
    print(i,end=',')
'''