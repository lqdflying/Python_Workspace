# -*- coding: utf-8 -*-
'''
Created on 2017年7月18日

@author: anddy.liu
'''
import os
import sys
print(__file__)  #只是因为在pydev里边，实际上这个命令打印的是相对路径，仅仅有一个文件名
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #获取当前目录的上上级父目录
sys.path.append(BASE_DIR) #加入模块寻找的path中
from mudule import login #path中有了模块目录，这样才能import
login.login("liuqd")