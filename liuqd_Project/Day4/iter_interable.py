# -*- coding: utf-8 -*-
'''
Created on 2017年7月16日

@author: anddy.liu
'''
from collections import Iterable
from collections import Iterator

print(type("name"),"--是否是可迭代对象-->",isinstance("name",Iterable))
print(type(123),"--是否是可迭代对象-->",isinstance(123,Iterable))
print(type([1,2,3]),"--是否是可迭代对象-->",isinstance([1,2,3],Iterable))
print(type({"name":"liuqd","age":23}),"--是否是可迭代对象-->",isinstance({"name":"liuqd","age":23},Iterable))
print(type(("name",1)),"--是否是可迭代对象-->",isinstance(("name",1),Iterable))
print(type((x for x in range(10))),"--是否是可迭代对象-->",isinstance((x for x in range(10)),Iterable))
#这里的(x for x in range(10))和generator.py里的name_generator = (str(i).upper() for i in names)没有什么不同
print("*可以被next()函数调用(也就是支持next方法)并不断返回下一个值的对象称为迭代器：Iterator。因此迭代器和可迭代对象不是一回事")
print("分割线".center(50,"+"))
print(type("name"),"--是否是迭代器-->",isinstance("name",Iterator))
print(type(123),"--是否是迭代器-->",isinstance(123,Iterator))
print(type([1,2,3]),"--是否是迭代器-->",isinstance([1,2,3],Iterator))
print(type({"name":"liuqd","age":23}),"--是否是迭代器-->",isinstance({"name":"liuqd","age":23},Iterator))
print(type(("name",1)),"--是否是迭代器-->",isinstance(("name",1),Iterator))
print(type((x for x in range(10))),"--是否是迭代器-->",isinstance((x for x in range(10)),Iterator))
print("*生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。\
除了int不行，其他的比如：list、dict、str等Iterable变成Iterator都可以使用iter()函数：")
print("分割线".center(50,"+"))
print(type("name"),"--使用iter函数变成迭代器-->",isinstance(iter("name"),Iterator))
#print(type(123),"--使用iter函数变成迭代器-->",isinstance(iter(123),Iterator))
print(type([1,2,3]),"--使用iter函数变成迭代器-->",isinstance(iter([1,2,3]),Iterator))
print(type({"name":"liuqd","age":23}),"--使用iter函数变成迭代器-->",isinstance(iter({"name":"liuqd","age":23}),Iterator))
print(type(("name",1)),"--使用iter函数变成迭代器-->",isinstance(iter(("name",1)),Iterator))