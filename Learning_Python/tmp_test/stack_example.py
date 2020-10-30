###
# File: stack_example.py
# Created Date: 2020-10-04
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday October 30th 2020 5:45:41 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
def hello(x):
    if x==1:
        return "op"
    else:
        u=1
        e=12
        s=hello(x-1)
        e+=1
        print(s)
        print(x)
        u+=1
    return e

hello(4)
def add(x, y):
    return x + y

def test(n):
    if n == 0:
        return 0
    else:
        return add(n, test(n - 1))
print(test(3))
