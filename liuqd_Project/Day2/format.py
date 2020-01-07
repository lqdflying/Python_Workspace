# -*- coding: utf-8 -*-
'''
Created on 2017年7月7日

@author: anddy.liu
'''
name = "my name is {},ang age is {}"

print("第一种format方法：",name.format("liuqd", 23))

name = "my name is {1},and age is {0}" #{}里的0或1是序号，用来代表format里的数据位置

print("第二种format方法：",name.format("liuqd", 23))  #这里我故意写错，你会在output里发现我的不同

name = "my name is {name},and age is {age}" #{}里写上名字，就像变量，下边可以赋值

print("第三种format方法：",name.format(name = "liuqd",age = 23))  #这里我故意写错，你会在output里发现我的不同

name = "my name is {name},and age is {age}" #{}里写上名字，就像变量，下边可以赋值

print("第四种format方法：",name.format_map({"name":"liuqd","age":23}))  #第四种是使用format_map的方法而不是format，语法也会有不同