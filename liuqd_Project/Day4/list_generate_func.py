# -*- coding: utf-8 -*-
'''
Created on 2017年7月14日

@author: anddy.liu
'''
names = ["LiuQuandong","LiuMing",["name1","name2"],"WuHongwei"]
print(type(names))
#需求是把names这个list的所有值全部变大写
#低逼格写法：码畜
m = []
for i in names:
    i = str(i).upper()
    m.append(i)
print(m,type(m))
#中逼格写法，码农
othername = [ str(i).upper() for i in names]
#一个列表生成式，就实现了要的功能，代码还少，先把list的值强制转为str，然后使用lower功能全部转小写
print(othername,type(othername))