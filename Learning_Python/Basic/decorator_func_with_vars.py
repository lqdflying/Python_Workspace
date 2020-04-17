# -*- coding:utf-8 -*-
###
# File: decorator_func_with_params.py
# Created Date: 2020-04-17
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday April 17th 2020 10:48:52 pm
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
        if not args:
            print("这个function没有参数")
        else:
            print("这个function的参数是",args)
        return func(*args)
    return wrapper

@use_logging
def foo(var=''):
    print("i am foo")

@use_logging
def bar(var=''):
    print("i am bar")

foo()
bar('liu')