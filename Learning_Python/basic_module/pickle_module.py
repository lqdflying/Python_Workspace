# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: anddy.liu
'''
import pickle

info = {
    "name":"liuqd",
    "age":"23"
    }

my = {
    "name":"quandong",
    "age":"55"
    }
print("[两种]正确的pickle序列化方法".center(50,"+"))
with open("liuqd.pickle","wb") as file:
    file.write(pickle.dumps(my))
    
print('pickle.dumps是格式化为内存中的字符串，也就是二进制的str流：，可以打印输出，但输出是乱码：\n',pickle.dumps(info))

with open("liuqd1.pickle","wb") as file1:
    pickle.dump(my,file1)


print("[两种]正确的pickle反序列化方法".center(50,"+"))
with open("liuqd.pickle","rb") as file:
    print(pickle.loads(file.read()))
    
with open("liuqd1.pickle","rb") as file1:
    print(pickle.load(file1))