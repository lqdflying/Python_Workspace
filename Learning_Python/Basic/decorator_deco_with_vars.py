# -*- coding:utf-8 -*-
###
# File: decorator_deco_with_vars.py
# Created Date: 2020-04-17
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday April 17th 2020 11:21:31 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
user,pwd = "liu","123"

def auth(auth_type):#1
    print("第一层参数:装饰器参数",auth_type) 
    def outer(func): #2
        print("第二层参数:被装饰函数的地址 ",func) 
        def wrapper(*args,**kwargs): #3
            print("第三层参数:被装饰的函数的参数的地址",*args,**kwargs) 
            if auth_type == "local": #4
                username = input("enter your name:").strip()
                passwd = input("enter your passwd:").strip()
                if user == username and pwd == passwd:
                    print("输入正确")
                    return func(*args,**kwargs)#5
                else:
                    print("认证失败,不触发return")
#                     return func(*args,**kwargs) #这句不该有，因为认证失败，就不该return被装饰函数去执行
            elif auth_type == "remote": 
                print("真实情况下，这里会调用remove认证的函数,这里先假设远程认证成功,触发return")
                return func(*args,**kwargs)
            print("这句永远不会执行,除非前边的if条件判断没有触发return")
        return wrapper  #6
    return outer #7
@auth(auth_type="remote")
def index():
    print("welcome to index page:这句话不会被打印,除非远程认证通过")
@auth(auth_type = "local")  #8
#home重新解析为：function: <function auth.<locals>.outer.<locals>.wrapper at 0x00000000037411E0>
def home():
    print("local方式认证——看到这一句，就是被装饰的函数自己真正的代码开始执行了")
    return("这里需要打印一些东西")

print("remote方式的认证".center(40,"+"))
index()
print("local方式的认证".center(40,"+"))
home()