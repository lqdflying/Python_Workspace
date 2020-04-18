# -*- coding:utf-8 -*-
###
# File: file_get_path.py
# Created Date: 2020-04-18
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday April 18th 2020 5:14:55 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import os
print("这个返回结果是一定的,是当前执行python命令所在的路径:\n",os.getcwd())
print("具体执行目标是相对路径,则__file__返回相对路径,反之返回绝对路径:\n",__file__)
print("返回__file__的basename:\n",os.path.basename(__file__))
print("返回__file__的dirname:\n",os.path.dirname(__file__))
print("切换到目标文件所在的目录下")
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("这个返回结果是一定的,是当前执行python命令所在的路径:\n",os.getcwd())
print("具体执行目标是相对路径,则__file__返回相对路径,反之返回绝对路径:\n",__file__)
print("返回__file__的basename:\n",os.path.basename(__file__))
print("返回__file__的dirname:\n",os.path.dirname(__file__))