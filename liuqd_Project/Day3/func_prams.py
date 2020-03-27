# -*- coding: utf-8 -*-
'''
Created on 2017年7月11日

@author: anddy.liu
'''
def func3(x,y,z):
    print(x,y,z)
def func4(x,y=2):  #这里就加了个默认参数
    print(x,y)


func3(1,2,3) #位置参数法方法调用，执行成功
func3(x=1,z=4,y=3) #关键字方法调用，执行成功
func3(1,2,z=5) #位置参数和关键字参数混合调用，成功
#func3(1,z=5,3) #报错
#func3(1,y=5,3) #报错
func3(1,z=5,y=3) #这样也是成功的
#结论：混合调用是可以的，但是关键字参数不能写在位置参数前边

func4(1) #利用了默认参数


def  func5(*liuqd): #参数组是用来传入不确定数量的参数
    print(type(liuqd)) #Python实际上是把参数组传入后变成一个tuple（元组）
    print(liuqd)

func5(1,2,3,4,5)
func5(*[1])

def func6(a,b,*args): #参数组一定要放在最后，然后前边的形参可以是多个,这里不因要写args，但是规范都是这么写
    print(a)
    print(b)
    print(args)

func6(1,2,3,4,5)

def func7(**kwargs): #参数组一定要放在最后，然后前边的形参可以是多个,这里加两个*，配合kwargs，出来的就是★ 字典★ 
    print("------->")
    print(type(kwargs))
    print(kwargs["name"])
    print(func4(kwargs["name"])) #函数内部再调用函数

func7(name="liuqd",my=8) #这样就是可以的，但是8=“m与”就不行——"变量名的第一个字符不能是数字"我觉得与这个规则有关

