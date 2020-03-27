# -*- coding: utf-8 -*-
'''
Created on 2017年7月18日

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
#以下是个错误的示范
'''
with open("liuqd.json","a+",encoding = "utf-8") as f:
    f.write(info)
这里会报错，提示TypeError: write() argument must be str, not dict
'''
# with open("liuqd.json","a+",encoding = "utf-8") as f:
#     f.write(str(info))
#这也是错误的，不够通用的处理办法
print("[两种]正确的json序列化方法".center(50,"+"))
with open("liuqd.json","w",encoding = "utf-8") as file:
    file.write(json.dumps(info))

with open("liuqd1.json","w",encoding = "utf-8") as file1:
    json.dump(my,file1)


