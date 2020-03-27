# -*- coding: utf-8 -*-
'''
Created on 2017年7月25日

@author: anddy.liu
'''
import sys
import liuqd_mode,mode2 #这里没有加path，因为模块和被调用脚本都在同一级,同时这里也演示了同时导入两个模块的办法  @UnresolvedImport
liuqd_mode.say_hello()
mode2.mode2_print()

'''
#第二种调用方法
from liuqd_mode import *  # @UnresolvedImport @UnusedWildImport
say_hello()
liuqd_print()
# def mode2_print():
#     print("main")
#一定不要import *，如果*，代表会把liuqd_mode里的所有def都会copy到这里编译一次，而后边又出现了def mode2_print()，那么则会把上边的覆盖掉
'''
'''
第三种导入方法，换名字导入
from liuqd_mode import say_hello as say_liuqd  # @UnresolvedImport
say_liuqd()
'''
'''
【一】
import liuqd_mode的本质就是把这liuqd_mode里的代码解释了一遍，然后统一整体赋值给一个新的变量，就叫liuqd_mode
想要调用，就加上liuqd_mode的模块名字+“点号”，再继续调用即可
【二】
from liuqd_mode import say_hello 这句的本质就是只把say_hello拿到当前位置编译执行一次，
想要调用的话，就直接say_hello()即可
'''

#import liuqd_mode_father  #直接当前import会报错的
print(sys.path)
#以下是输出
# ['E:\\Python_Learn\\Python_Workspace\\liuqd_Project\\First_project\\Day5\\module1', 
# 'E:\\Python_Learn\\Python_Workspace\\liuqd_Project\\First_project', 
# 'C:\\Users\\liuqd\\AppData\\Local\\Programs\\Python\\Python36\\DLLs', 
# 'C:\\Users\\liuqd\\AppData\\Local\\Programs\\Python\\Python36\\lib', 
# 'C:\\Users\\liuqd\\AppData\\Local\\Programs\\Python\\Python36', 
# 'C:\\Users\\liuqd\\AppData\\Local\\Programs\\Python\\Python36\\lib\\site-packages', 
# 'E:\\Python_Learn\\Python_Workspace\\liuqd_Project\\First_project\\mudule', 
# 'C:\\Users\\liuqd\\AppData\\Local\\Programs\\Python\\Python36\\python36.zip']

import os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
#这种append的方法就是加在最后的，那也就意味这需要遍历完所有的list，才能找得到'E:\\Python_Learn\\Python_Workspace\\liuqd_Project\\First_project\\Day5']
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
#采用insert的方法，就是放在最前边了
print(sys.path)
import liuqd_mode_father  # @UnresolvedImport @UnusedImport
liuqd_mode_father.say_hello() #这样就可以了

















