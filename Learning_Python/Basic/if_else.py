# -*- coding:utf-8 -*-
###
# File: if_else.py
# Created Date: 2020-05-03
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday May 3rd 2020 4:20:48 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
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
