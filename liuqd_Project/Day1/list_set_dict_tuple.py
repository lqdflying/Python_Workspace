# -*- coding: utf-8 -*-
'''
Created on 2017年7月4日

@author: liuqd
'''

name = "liuquandong"
name2 = name
print("My name is ",name,name2)

#name2这次的赋值直接指向了name的内存空间，那么下次name重新赋值就不会去改了
name = "liu ming"
#print(type(name)) #这样的写法是打印数据类型，以便尝试查看数据类型
print(name[1:3]) #字符串切片打印，顾头不顾尾，尾部的3位置处的数据不打印

# givemevar = input("give my a tar:")
# 
# print(givemevar)


# 小技巧，Ctrl+？会把
# 光标选择的
# 多行前边加上井号注释掉
list1 = [1,2,3]
list1_1 = list([1,2,3])
list2 = set([1,2,55,66,4])
list3 = {1:2,3:4}
list4 = ("liuquandong","liuming")

print(list1,type(list1))
print(list1_1,type(list1_1))
print(list2,type(list2))
print(list3,type(list3))
print(list4,type(list4))