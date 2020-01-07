# -*- coding: utf-8 -*-
#@UnresolvedImport
#@UnusedVariable
'''
Created on 2019年4月19日

@author: anddy.liu
'''
def stu_register(name,age,*my_tuple,**my_dict):
    print(name,age,my_tuple,my_dict)
stu_register("liuqd",32,"myname","newname",city = "shanxi") 
some_name = ["11", "nothing", "gogo", "another gogo"]
some_dict = {'city': 'shanxi', "gogo": "feeling"}
stu_register("liuqd", *some_name, **some_dict)
#注意这里的传参,city = "shanxi"是传给dict的,city是key,不能用引号括起来
import platform
print(platform.python_version())