# -*- coding: utf-8 -*-
'''
Created on 2017年7月6日

@author: liuqd
'''
msg = "我爱北京天安门"
msg_encode = msg.encode(encoding='utf_8', errors='strict')
print("以utf-8编码-->  ",msg.encode(encoding='utf_8', errors='strict')) #encode的时候，如果没有指定编码，encoding就用utf-8

print("以GBK编码-->  ",msg.encode(encoding='GBK', errors='strict')) #encode的时候，如果没有指定编码，encoding就用utf-8

print("反编码一个东西-->  ",msg_encode.decode())  #默认解码也是utf-8
print("反编码一个东西-->  ",msg_encode.decode(encoding='utf_8', errors='strict'))