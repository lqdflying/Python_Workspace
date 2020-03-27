# -*- coding: utf-8 -*-
'''
Created on 2017年7月14日

@author: anddy.liu
'''
names = ["LiuQuandong","LiuMing",["name1","name2"],"WuHongwei"]
print(names[0])
#print(type(names))
#需求是把names这个list的所有值全部变大写
#中逼格写法，码农
#othername = [ str(i).upper() for i in names]
#把上边的列表生成式改成小括号，就是生成器
print(type((str(i).upper() for i in names)))
name_generator = (str(i).upper() for i in names)
print(type(name_generator))
print(name_generator)
'''
name_generator = (str(i).upper() for i in names)
#print(name_generator[0]) 这句会报错，因为根本没有生成还
print(name_generator.__next__()) #调用next方法是可以的，生成器的专用方法,
print(name_generator.__next__())
for i in name_generator:
    print(i)

#【注】：生成器只有在调用时才会生成相应的数据,
#【注】：生成器只能next，不能previous。只能一步一步后滚，不能前滚，不能跳步？
'''