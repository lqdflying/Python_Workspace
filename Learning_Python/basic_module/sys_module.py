# -*- coding: utf-8 -*-
'''
Created on 2018年3月3日

@author: anddy.liu
'''
import sys
# import os
# # print("argv的第0号元素是程序本身的路径：\n",sys.argv[0])
# # print("argv的第1号元素是程序py文件接收的第一个外部参数：\n",sys.argv[1])
# # print("argv的第2号元素是程序py文件接收的第一个外部参数：\n",sys.argv[2])
# # if sys.argv[1] == 'a' and sys.argv[2] == 'b':
# #     sys.exit(0)
# # else:
# #     sys.exit(1)
# print("获取python解释程序的当前版本： \n",sys.version)
# print("返回操作系统平台命令： \n",sys.platform)
# print("返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值：\n",sys.path)
# print("有时候需要添加我们自己写的module的路径，其实就是修改sys.path的值")
# sys.path.insert(0,'E:\Python_Learn\Python_Workspace\\') #增加了目录
# print("查看添加自己的路径以后的变量的返回值：\n",sys.path)
# sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\module') 
# print("一个典型的把父目录下的统计子目录module作为第一模块搜索路径的语法案例：\n",sys.path)
# print("返回系统导入的模块字段，key是模块名，value是模块:\n",sys.modules)
sys.stdout.write('please:\n')
name=sys.stdin.readline()[:-1]
print ('Hi, %s!' %name)