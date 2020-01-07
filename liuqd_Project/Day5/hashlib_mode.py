# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import hashlib
print("同一段str分别用md5和sha256加密后的结果展示：\n")
m = hashlib.md5()
m.update(b"liuqd")
print("md5加密：",m.hexdigest()) #十六进制格式的hash
f = hashlib.sha256()
f.update(b"liuqd")
print("sha256加密：",f.hexdigest())
print("\n展示只要字符串是一样的，不管最终字符串是如何生成的，md5都是一样的：\n")
m.update(b"quandong")
print("一段str分两次拼成：",m.hexdigest()) #十六进制格式的hash
n = hashlib.md5()
n.update(b"liuqdquandong")
print("一段str一次性输入：",n.hexdigest()) #拼成一个和分别update两次得到的md5是一样的
print("中文内容加密的结果：\n")
h = hashlib.md5()
h.update("liuqd加密啊加密啊".encode(encoding='utf_8', errors='strict'))
print("中文加密：",m.hexdigest()) 
