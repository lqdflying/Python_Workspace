# -*- coding:utf-8 -*-
###
# File: exception_example.py
# Created Date: 2020-05-02
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 2nd 2020 2:18:16 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
while True:
    try:
        x = input("请输入一个数字: ")
        if not x.isdigit():
            raise ValueError("x不能是字母")
    except ValueError:
        print("您的输入必须是数字,不能是字母")
        raise
    else:
        try:
            if int(x) >= 5:
               raise ValueError("x 必须是小于5数字")
            print("您输入了正确的小于5的数字")
            break
        except ValueError:
            print("您输入的不是小于5的数字！")
            # raise #这里加上了raise,就会跳出while,因为raise会抛出异常,然后程序执行结束,不加raise才能循环
    finally:
        print("finally".center(20,"+"))
        print("这是个样例,证明不管错误与否,finally里的语句都会执行")