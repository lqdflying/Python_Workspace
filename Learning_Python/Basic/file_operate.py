# -*- coding:utf-8 -*-
###
# File: file_operate.py
# Created Date: 2020-04-18
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday April 18th 2020 4:43:43 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import os
currentdir = os.path.dirname(__file__)
print("以a+方式打开文件并且想输出的话,必须使用seek(0)让指针回到文件句柄开始,否则不报错但也无输出")
with open("%s/liuqdarticle.txt"%currentdir,"a+",encoding = "utf-8") as liuqdfile: 
#注意，如果是追加，那么需要使用a的方式打开文件,也就是append，但是append的方式依然不能行写
    #liuqdfile.write("\n天安门上太阳升")
    liuqdfile.seek(0)
    print(liuqdfile.read()) #有这一行会报错
print("以a方式打开文件并且想输出的话,必须使用seek(0)让指针回到文件句柄开始,否则不报错但也无输出")
with open("%s/liuqdarticle.txt"%currentdir,"r+",encoding = "utf-8") as liuqdfile: 
#注意，如果是追加，那么需要使用a的方式打开文件,也就是append，但是append的方式依然不能行写
    #liuqdfile.write("\n天安门上太阳升")
    #liuqdfile.seek(0)
    print(liuqdfile.read()) #有这一行会报错

a = open("liuqdarticle.txt","a+",encoding = "utf-8")
a.seek(0)
print(a.read())
a.close()