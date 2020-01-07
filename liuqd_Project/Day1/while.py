# -*- coding: utf-8 -*-
'''
Created on 2017年7月5日

@author: liuqd
'''
count = 1
while count <= 10:
    name = input("Enter the name:")
    if name == "liuqd":
        print("第",count,"次输入成功","正确的结果是",name)
        break
    else:
        print("第",count,"次输入错误")
        count = count+1
        
print("你在成功之前错误的尝试了",count-1,"次")