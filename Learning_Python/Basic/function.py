# -*- coding: utf-8 -*-
'''
Created on 2017年8月28日

@author: anddy.liu
'''
def hello() :
    print("第一个函数：hello world！")

#调用hello()函数
hello()
#这种没有参数的函数编程其实就是面向过程编程

#嵌套函数
def my_max4(a,b,c,d):
    res1=my_max(a,b)
    res2=my_max(res1,c)
    res3=my_max(res2,d)
    return res3
def my_max(x,y):
    res=x if x >y else y
    print("return才是函数的返回值,这里不会输出,除非直接调用")
    return res
    
print("嵌套函数".center(30,"+"))
print(my_max(3,4))
print(my_max4(1,20,3,4))
my_max(100,99)
#递归函数
def calc(n):
    print(n)
    if int(n/2) > 0:
        return calc(n/2)
    print("->",n)
print("递归函数".center(30,"+"))    
calc(10)  #这样写就不会出现死循环了，因为上边加了条件


#匿名函数
# 可写函数说明
getsum = lambda arg1, arg2: arg1 + arg2
# 调用sum函数
print("匿名函数".center(30,"+"))    
print ("相加后的值为 : ", getsum( 10, 20 ))
print ("相加后的值为 : ", getsum( 20, 20 ))

#不定长参数
def stu_register(name,age,*my_tuple,**my_dict): 
# 一个*的变长参数最终定义是一个tuple，两个**的变长参数最终定义是一个dict，只要是出现一个*或两个**，后边的名字无所谓，不一定要是*args或**kwargs
    print(name,age,my_tuple,my_dict)

stu_register("liuqd",32,"myname","newname",city = "shanxi")

#高阶函数
def add(x,y,f):
    return f(x) + f(y)

res = add(3,-6,abs) #abs是内建函数，就是求绝对值
print("高阶函数".center(30,"+"))    
print(res)
