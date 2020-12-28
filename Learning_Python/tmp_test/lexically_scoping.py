###
# File: lexically_scoping.py
# Created Date: 2020-12-28
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Monday December 28th 2020 10:37:01 am
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
# Python is a statically scoped and a lexically scoped language. 
# 词法作用域关注函数在何处声明,而动态作用域关注函数从何处调用
def foo():
    print(a)
def bar():
    a = 3
    def goo():
        return a
    foo()
    print(goo())

a = 2
bar()