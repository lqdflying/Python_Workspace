###
# File: stack_example.py
# Created Date: 2020-10-04
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday October 4th 2020 9:27:07 am
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