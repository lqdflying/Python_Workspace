# -*- coding:utf-8 -*-
###
# File: main_example.py
# Created Date: 2020-04-26
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Monday April 27th 2020 10:54:09 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
foo = 0
def my_max4(a,b,c,d):
    res1=my_max(a,b)
    res2=my_max(res1,c)
    res3=my_max(res2,d)
    print(res3)
def my_max(x,y):
    res=x if x >y else y
    return res

def show():
    print(foo)

'''
Code snippet for a `if __name__ == "__main__": ...` block (Python)
if __name__ == "__main__":
    pass
'''

if __name__ == "__main__":
    print(__name__) #print(__name__) #输出结果是__main__
    my_max4(1,20,3,4)


'''
print("输出__name__的值:",__name__) #print(__name__) #输出结果是__main__
my_max4(1,20,3,4)
'''