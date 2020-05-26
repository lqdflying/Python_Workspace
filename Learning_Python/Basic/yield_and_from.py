# -*- coding:utf-8 -*-
###
# File: yield_and_from.py
# Created Date: 2020-05-24
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Tuesday May 26th 2020 3:05:37 pm
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

def coroutine_while(father):
    while True:
        result = yield from coroutine_example(father)
        return f"coroutine_while()的返回值[\n\t{result}\n\t]"

def coroutine_again(father):
    while True:
        result = yield from coroutine_while(father)
        return f"coroutine_again()的返回值--->{result}<---"

print("直接调用子生成器".center(30,"+"))

coro_child = coroutine_example('quan')
coro_child.send(None)
# coro_child.send(None) #第二次send(None)会触发异常

print("直接调用委派生成器".center(30,"+"))
coro_while = coroutine_while('dong')
coro_while.send(None)
# coro_while.send(None) #第二次send(None)会触发异常

print("for循环调用委派生成器".center(30,"+"))
coro_for = coroutine_while('dong')
coro_for.send(None)
# for i in ['1', None]:
#     print(coro_for.send(i)) #send(None)会触发异常

print("for循环调用二级委派生成器".center(30,"+"))
coro_again = coroutine_again('second')
coro_again.send(None)
for i in ['1', None]:
    try:
        print(coro_again.send(i)) #send(None)会触发异常
    except StopIteration as a:
        print(a.value)
    


print("try-except调用委派生成器".center(30,"+"))
coro = coroutine_from('liu')
coro.send(None)
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