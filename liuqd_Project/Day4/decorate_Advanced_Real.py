# -*- coding: utf-8 -*-
'''
Created on 2017年7月13日

@author: anddy.liu
'''
'''
写装饰器记住三个关键：
    1、被装饰函数的内存地址一定要传进去，并且在装饰器内无影响和修改的执行
    2、被装饰函数要在外边套一层壳之后，再return回来，重新赋给被装饰函数来调用
    3、被装饰函数传进去和套了壳以后要传return回来的函数，形参都要和被装饰函数实际的形参一致，如果不好判断，就直接使用*agrs,**kewagrs来统配即可
'''


user,pwd = "liuqd","abc123"

def auth(auth_type):#这个装饰器只是在入口传了个实参进来，这个实参贯穿整个auth始终都有效
    print("第一层参数:",auth_type) 
    def outer(func): 
        print("第二层参数:",func) 
        def wrapper(*args,**kwargs): 
            print("第三层参数:",*args,**kwargs) 
            if auth_type == "local": 
                username = input("enter your name:").strip()
                passwd = input("enter your passwd:").strip()
                if user == username and pwd == passwd:
                    print("输入正确")
                    res = func(*args,**kwargs)
                    return res
                else:
                    exit("验证失败")
            elif auth_type == "remote":
                print("remote不会,会把这个函数给透过")
        return wrapper  
    return outer #auth最终的结果是返回了里边的函数outer，所以实际上是outer的形参接收装饰器传入的被装饰的原函数的内存地址

def index():
    print("welcome to index page:")
#@auth(auth_type = "local")  
#home重新解析为：function: <function auth.<locals>.outer.<locals>.wrapper at 0x00000000037411E0>
def home():
    print("welcome to home page")
    return("这里需要打印一些东西")
'''
这种装饰器的解释：
    auth(auth_type = "local") #auth预传参
    auth的最终结果是回传outer的内存地址
所以最终是home = outer(home)，实际上是home = wrapper(),而wrapper里的func是原有的home，
[额外解释一句，auth返回了outer，outer又返回了wrapper，那实际上就是返回了wrapper]
home变成了包裹着wrapper外衣的home，所以wrapper和func都的形参都是*agrs，**keargs
所以结果就是：{wrapper[home(原)→ func)]}→home
这里参考decorator_demoParams.py，实际上就是把decorator_demoParams里的input换成了auth(auth_type = "local")
'''
@auth(auth_type = "remote") 
#[15]bbs重新解析为：function: <function auth.<locals>.outer.<locals>.wrapper at 0x0000000003741840>
def bbs():
    print("welcome to bbs page")

index()
print(home())
bbs()