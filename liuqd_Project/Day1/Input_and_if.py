# -*- coding: utf-8 -*-
'''
Created on 2017年7月5日

@author: liuqd
'''
#import getpass #C语言里是include
name = input("name:")
password = input("passwd:")

info='''
============ info of {liu_name} ======
Name:{liu_name}
Password:{liu_password}
============================
'''.format(liu_name=name,
           liu_password=password
           )
forname = "liuqd"
forpwd = "123"
if forname == name and forpwd == password : #注意这里的冒号不能少，少了Python不认

    print(info)
elif forname != name and forpwd == password:
    print("other option")
else:
    print("failed")
#python要求强制缩进，不然会报错，Python靠缩进来搞定子代码的语句块
