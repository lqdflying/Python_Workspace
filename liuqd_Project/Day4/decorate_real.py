# -*- coding: utf-8 -*-
'''
Created on 2017年7月13日

@author: anddy.liu
'''

import time
'''
def deco(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("the func run time is %s"%(stop_time-start_time))

def deco1(func):
    start_time = time.time()
    return func
    stop_time = time.time()
    print("the func run time is %s"%(stop_time-start_time))
'''
'''
def test1():
    time.sleep(2)
    print("in the test1")
    
def test2():
    time.sleep(2)
    print("in the test2")
print("分割线,第一种调用，传参是函数".center(50,"+"))
deco(test1)  #千万不能加括号，写成test1()
deco(test2)  #千万不能加括号，写成test2()
print("分割线,另一种调用，返回值是函数".center(50,"+"))
test1 = deco1(test1) #千万不能加括号，写成deco1(test1())
test1()
test2 = deco1(test2) #千万不能加括号，写成deco1(test1())
test2()
print("分割线,这里才像个装饰器".center(50,"+"))
test1 = timier(test1)
test1()

'''
def timier(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        print("开始执行")
        #return func(*args,**kwargs) #使用这种写法，后边的步骤就不会执行了，等于装饰了一半
        func(*args,**kwargs)#这种写法，适用于需要得到被装饰函数执行前和执行后状态的那种
        stop_time = time.time()
        print("the func run time is %s"%(stop_time-start_time))  
    return deco   


print("分割线,这里真正变成了装饰器的写法".center(50,"+"))
@timier   #这里是个语法糖，来实现上边的test3 = timier(test3)这种问题,
def test3():
# 如果想要给这个函数增加timier功能功能，就要在这个函数的头部添加@timier，
# 这个语法糖等同于：test3 = timier(test3),实际上是test3 = deco(),而deco里的func是原有的test3，
# test3变成了包裹着deco外衣的test3，所以deco和func都的形参都是*agrs，**keargs
    time.sleep(2)
    print("in the test3")
test3()

'''
test3 = timier(test3)的功能有那么几个：
    1、把test3的内存地址传递给timier，赋值给形参func：timier(test3)
        a、timier把test3的内存地址传递给func(*args,**kwargs),这种写法可以保证不管test3有几多变量都能hold住
    2、timier把内部定义的deco的内存地址传递给test3
所以结果就是：{deco[test3(原)→ func)]}→ test3
'''

print("带参数的装饰器".center(50,"+"))
@timier
def test2(name):
    time.sleep(2)
    print("in the test2:----> %s"%(name))

@timier
def test5(name,age):
    time.sleep(2)
    print("in the test5:----> %s 年龄是：%s"%(name,age))

test2("liuqd")
test5("liuqd",32)





