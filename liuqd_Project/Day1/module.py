# -*- coding: utf-8 -*-
'''
Created on 2017年7月6日

@author: liuqd
'''
#import sys
#import os
'''
print(sys.argv) #sys是一个模块，调用模块/库里的方法就用点号

#cmd_res = os.system("dir") #os.system这个命令一调用就执行了，结果是直接输出到屏幕上的，而不是存给变量的，仅仅是返回一个命令成功的标识：0
os_res = os.popen("dir").read() #采用read读取内存数据，返回的就是dir正确的命令结果，不加read()，返回就是内存地址
#print("-->",cmd_res)  #因此这里会发现，最后打印是个0
print("-->",os_res)  #因此这里会发现，最后打印是正确的，并且中文显示也是正常的

#os.mkdir("testdir")  #这个命令可以用来建立目录
'''
