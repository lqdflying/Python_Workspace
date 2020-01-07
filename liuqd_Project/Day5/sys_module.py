# -*- coding: utf-8 -*-
'''
Created on 2017年8月2日

@author: anddy.liu
'''
import sys
import os
print(sys.version)
print("加入模块搜索路径前的PATH",sys.path)
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #一定要用insert的方式，如果是用append，那么path就是在最后的，就会变成遍历
print("加入模块搜索路径后的PATH",sys.path)
#sys.exit(0) #退出程序，正常退出时exit(0)
print("arge parameter display here :\n",sys.argv) #命令行参数List，第一个元素是程序本身路径