# -*- coding: utf-8 -*-
'''
Created on 2017年7月13日

@author: anddy.liu
'''
user,pwd = "liuqd","abc123"

def auth(auth_type):#1
    print("第一层参数:",auth_type) 
    def outer(func): #2
        print("第二层参数:",func) 
        def wrapper(*args,**kwargs): #3
            print("第三层参数:",*args,**kwargs) 
            if auth_type == "local": #4
                username = input("enter your name:").strip()
                passwd = input("enter your passwd:").strip()
                if user == username and pwd == passwd:
                    print("输入正确")
                    return func(*args,**kwargs)#5
                else:
                    exit("验证失败")
            elif auth_type == "remote": 
                print("remote不会,会把这个函数给透过")
        return wrapper  #7
    return outer #8
@auth(auth_type="remote")
def index():
    print("welcome to index page:这句话不会被打印")
@auth(auth_type = "local")  
#home重新解析为：function: <function auth.<locals>.outer.<locals>.wrapper at 0x00000000037411E0>
def home():
    print("welcome to home page")
    return("这里需要打印一些东西")
home()
index()