# -*- coding:utf-8 -*-
###
# File: yield_and_from.py
# Created Date: 2020-05-24
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Thursday May 28th 2020 9:49:26 pm
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
    print('coroutine_while: start')
    while True:
        result = yield from coroutine_example(father)
        print('coroutine_while: end')
        return f"coroutine_while()的返回值[\n\t{result}\n\t]"

def coroutine_again(father):
    print('coroutine_again: start')
    while True:
        result = yield from coroutine_while(father)
        print('coroutine_again: end')
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

for i in [2 ,3, 4, 5, None]:
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
    return "fab task done!"
    
f = fab(5)
g = fab(6)
'''
f.__next__()
print(f.__next__()) #1
print(f.__next__()) #2
print(f.__next__()) #3
print(f.__next__()) #5
# print(f.__next__()) #StopIteration
'''

print(type(f))
print("处理异常方法一:不能catch最终生成器的返回值:")
for i in f:
    print(i,end=' ') #针对生成器使用for调用也能自动的处理StopIteration异常
print("\n处理异常方法二:可以catch最终生成器的返回值:")
while True:
    try:
        print(g.__next__(),end=' ')
    except StopIteration as e:
        print('\n',e.value)
        break

def f_wrapper(n):
    print('\nstart')
    for item  in fab(n):
        yield item
    print('\nend')

wrap = f_wrapper(5)
for i in wrap:
    print(i,end=',')

def f_wrapper2(n):
    print('start')
    last_result = yield from fab(n)  #注意此处必须是一个可生成对象
    print('\n最后委派生成器return结束的返回值是:',last_result)
    print('\nend')
wrap = f_wrapper2(5)
print("初始化委派生成器,而它返回的是子生成器的第一个值:",wrap.__next__())
for i in wrap:
    print(i,end=',')