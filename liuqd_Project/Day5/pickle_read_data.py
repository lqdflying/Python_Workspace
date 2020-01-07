# -*- coding: utf-8 -*-
'''
Created on 2017年7月18日

@author: anddy.liu
'''
import pickle
print("[两种]正确的pickle反序列化方法".center(50,"+"))
with open("liuqd.pickle","rb") as file:
    print(pickle.loads(file.read()))
    
with open("liuqd1.pickle","rb") as file1:
    print(pickle.load(file1))