# -*- coding: utf-8 -*-
'''
Created on 2017年8月2日

@author: anddy.liu
'''
import os
import time
print("获得当前目录",os.getcwd())
os.chdir(r"E:\Python_Learn\Python_Workspace\liuqd_Project\First_project") #Change the current working directory to path
print("使用chdir改变目录：\n",os.getcwd())
print("使用curdir再次返回到当前目录：\n",os.curdir) #返回当前目录
print("返回当前目录的父目录：\n",os.pardir) #返回当前目录的父目录
#os.makedirs(r"E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\liuqd\liu\qd") #递归建目录
#os.removedirs("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\liuqd\liu\qd") 
#递归删除目录：如果目录为空则删除，并递归到上一层目录，上一层还是为空，继续删除，以此类推
#os.mkdir("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\liuqd\liu\qd") #不能递归建立目录，只在存在的目录下建目录
#os.rmdir("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\liuqd\liu\qd") #不能递归删除空目录，只是删除同级子目录
print("返回当前目录下的子目录，会以list形式返回\n",os.listdir())
#os.remove() #删除一个文件
#os.rename() #重命名一个文件
print("返回文件或对象的属性，会是一个特殊的格式：\n",os.stat("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\Day1"))
print("输出操作系统特定的路径分隔符:\n",os.sep)
print("输出当前平台使用的行终止符:\n",os.linesep)
print("输出用于分割文件路径的字符串:\n",os.pathsep)
print("输出字符串指示当前使用平台:\n",os.name) #nt是Windows，Linux是posix
print("获取环境变量:\n",os.environ) #输出其实是一个字典
#os.system("ipconfig /all") #运行cmd或shell命令
print("显示当前文件的绝对路径:\n",os.path.abspath("os_module.py")) #
print("将path分割成目录和文件名二元组返回:\n",os.path.split("os_module.py")) #返回结果是 ('', 'os_module.py')
print("将path分割成目录和文件名二元组返回:\n",os.path.split("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\os_module.py")) 
#返回结果是E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\os_module.py
print("只取目录名:\n",os.path.dirname("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\os_module.py")) 
print("只取文件名:\n",os.path.basename("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\os_module.py")) 
print("判断是否是绝对路径:\n",os.path.isabs("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project\os_module.py")) 
print("判断是否是一个文件:\n",os.path.isfile("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project")) 
print("判断是否是一个目录:\n",os.path.isdir("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project")) 
print("获取文件的最后存取时间:\n",os.path.getatime("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project"))
print("获取文件的最后存取时间,并格式化后输出:\n",time.localtime(os.path.getatime("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project")))
print("获取文件的最后存取时间,并格式化后再format输出:\n",time.strftime("%A, %d %B %Y %H:%M:%S",time.localtime(os.path.getatime("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project"))))
print("获取文件的最后修改时间,并格式化后输出:\n",time.localtime(os.path.getmtime("E:\Python_Learn\Python_Workspace\liuqd_Project\First_project")))




