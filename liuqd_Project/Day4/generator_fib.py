# -*- coding: utf-8 -*-
'''
Created on 2017年7月14日

@author: anddy.liu
'''
def fib(num):
    n, a, b = 0, 0, 1
    while n < num:
        print(b)
        a, b = b, a + b  #这个赋值语句的含义等同于：a=b，b=a+b
        n = n + 1
    return "done"

#fib(100)
'''
上边这个斐波那契函数变成生成器只需要一部，就是yield替换print即可
yield的一个重大功能就是把一次循环从中间断开，由原来的
（循环[固化型，无法停止的自动执行一次return]1次）（循[固化型，无法停止的自动执行一次return]环2次）（循环[固化型，无法停止的自动执行一次return]3次）……
变为：
（循环一次*30%[需求型自主中断：在这里直接执行一次return] 循环剩余80%）（循环一次*30%[需求型自主中断：在这里直接执行一次return] 循环剩余80%）（循环一次*30%[需求型自主中断：在这里直接执行一次return] 循环剩余80%）
【注】：中断的含义是可以让程序去做别的事情了，直到使用next()或__next__()调用位置，都会保留当前中断状态，而不是像上边的while循环那样，没法控制，自动死脑筋的
一直执行下去，直到while条件不满足
'''
def fib_gene(num):
    n, a, b = 0, 0, 1
    while n < num:
        yield b  #yield有保存函数中断状态，并返回值
        a, b = b, a + b  #这个赋值语句的含义等同于：a=b，b=a+b
        n = n + 1
    return "done"

#print(fib_gene(10))
#输出结果是<generator object fib_gene at 0x00000000025C1888>，证明是这个是生成器
f = fib_gene(10)
print(next(f)) #第一次调用，fib_gene走到yield b就停止了，然后返回b，所以这里print会返回b的初始值1
print(next(f)) 
#第二次调用，fib_gene会从yield b提示的这里继续完成第一次while循环，这时候，b=a+b=0+1=1，
#然后while循环条件判断为true，开始第二次循环，这时候执行到yield b又停止了，返回b，注意现在的中断时处在第二次while循环这里
#但是因为没有走到下边a、b赋值这一步，所以yield返回的是上一次循环也就是第一次循环后的b的新值，也就是b=a+b=0+1=1
print(next(f))
#第三次调用next，这时候，while循环才开始执行yield以后的代码（注意现在还是处于第二次循环），b=3，之后while开始第三次循环，并继续在yield这里中断并返回第二次循环获得的值3
print(next(f))
print(next(f))
print(next(f))
print(next(f))
'''
这样就不会出错
for i in f:
    print(i)
'''
'''
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
一直这样打印是会输出异常的，下边会演示如何抓住异常
'''
    
'''
print("带异常处理".center(50,"+"))
g = fib_gene(8)

while  True:
    try:
        x = next(g) #生成器的调用方法之一
        print("g:",x)
    except StopIteration as e:
        print("generator return value:",e.value)
        break

print("带异常处理的另一种写法".center(50,"+"))
h = fib_gene(8)

while  True:
    try:
        x = h.__next__()  #其实是生成器的另一种调用方法
        print("h:",x)
    except StopIteration as e:
        print("generator return value:",e.value)
        break
'''
