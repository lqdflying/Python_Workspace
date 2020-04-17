# -*- coding:utf-8 -*-
###
# File: decorator_simple copy.py
# Created Date: 2020-04-17
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday April 17th 2020 6:18:08 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
def use_logging(func):
    def wrapper(*args, **kwargs):
        print("[The function]:%s is running" % func.__name__)
        return func(*args)
    return wrapper

@use_logging
def foo():
    print("i am foo")

@use_logging
def bar():
    print("i am bar")

bar()