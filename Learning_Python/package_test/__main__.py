# -*- coding:utf-8 -*-
###
# File: __main__.py
# Created Date: 2020-04-26
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Thursday April 30th 2020 3:58:35 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
# -*- coding: utf-8 -*-
'''
Created on 2018年3月30日

@author: anddy.liu
'''
import sys
import os
print("执行了__main__.py")
print('sys.path:', sys.path)
 
print('__main__.py的__name__变量 :', __name__)
print('__main__.py的__package__变量 :', __package__)
# print(os.path.dirname(__file__))
# print(os.pardir)

if not __package__: #如果__pachage_)为空,那么证明执行方式是python <dir>,而没有加-m
    path = os.path.join(os.path.dirname(__file__), os.pardir)
    sys.path.insert(0, path)
# print(path)
import package_test as first
first.main()
