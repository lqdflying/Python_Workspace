# -*- coding: utf-8 -*-
'''
Created on 2018年3月10日

@author: anddy.liu
'''
import json
info = {
    "name":"liuqd",
    "age":"23"
    }
my = {
    "name":"quandong",
    "age":"55"
    }
print("[两种]正确的json序列化方法，序列化就是生成文件，不管是内存中还是文件中".center(50,"+"))
with open("liuqd.json","w",encoding = "utf-8") as file:
    file.write(json.dumps(info))
print('json.dumps是格式化为内存中的字符串，也就是str流，可以打印输出，并且可见：\n',json.dumps(info))

with open("liuqd1.json","w",encoding = "utf-8") as file1:
    json.dump(my,file1)
    
print("[两种]正确的json反序列化序列化方法，反序列化就是直接从文件读取整个格式为字典".center(50,"+"))

with open("liuqd.json","r",encoding = "utf-8") as file:
    data = json.loads(file.read())
    print('json.loads的方法需要赋给一个对象，再输出:',data)

with open("liuqd1.json","r",encoding = "utf-8") as file1:
    print('json.load本身就是一个对象，直接可以print：',json.load(file1))