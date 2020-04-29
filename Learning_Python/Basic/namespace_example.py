# -*- coding:utf-8 -*-
###
# File: namespace_example.py
# Created Date: 2020-04-29
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday April 29th 2020 11:44:37 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import sys
import os
module_path = os.path.dirname(os.path.dirname(__file__))
sys.path.extend(['%s/namespace_package1/'%module_path, '%s/namespace_package2/'%module_path])
print(sys.path)
# import forfun.first as first
# import forfun.second as second
# first.fun1()
# second.fun2()
import forfun
print(forfun.__path__)
from forfun import first
from forfun import second
first.fun1() #实际上是不同路径的子包
second.fun2() #实际上是不同路径的子包