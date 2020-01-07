# -*- coding: utf-8 -*-
'''
Created on 2018年3月3日

@author: anddy.liu
'''
import os
import time
print("针对os.path类的操作".center(30,"+"))
print("返回path的绝对路径，这里的path就是两个点，也就是当前路径的父目录：\n",os.path.abspath('..'))
print("将路径分解为路径和文件名两个部分，结果是元组：\n",os.path.split('E:\Python_Learn\Python_Workspace\LearningPython\PythonLearn\\basic_module'))
#注意，这里使用\\b是因为\b是特殊字符，需要转义
print("如果路径最后仅是\,那么分解后的元组，文件名那一部分为空：\n",os.path.split('E:\Python_Learn\Python_Workspace\LearningPython\PythonLearn\\'))
#最后是两个\\也是为了转义
print("将路径分解为文件夹和文件名两个部分，结果只显示文件路径：\n",os.path.dirname('E:\Python_Learn\Python_Workspace\LearningPython\PythonLearn\\basic_module'))
print("将路径分解为文件夹和文件名两个部分，结果只显示文件名：\n",os.path.basename('E:\Python_Learn\Python_Workspace\LearningPython\PythonLearn\\basic_module'))
print("查看路径是否存在，存在返回true，否则返回false: \n",os.path.exists('E:\Python_Learn'))
print("如果path是绝对路径，则返回true，否则返回false: \n",os.path.isabs('E:\Python_Learn'))
print("如果path是一个文件而非目录，则返回true，否则返回false: \n",os.path.isfile('E:\Python_Learn'))
print("如果path是一个目录而非文件，则返回true，否则返回false: \n",os.path.isdir('E:\Python_Learn'))
print("将多个路径组合: \n",os.path.join('E:\\','Python_Learn'))#E:\\也是为了转义
print("返回文件或文件夹的最后修改时间",time.ctime(os.path.getmtime('E:\Python_Learn')))
print("返回文件或文件夹的创建时间",time.ctime(os.path.getctime('E:\Python_Learn')))
print("返回文件或文件夹的最后访问时间",time.ctime(os.path.getatime('E:\Python_Learn')))
print("返回文件或文件夹的最后修改时间，如果不加ctime进行格式化，显示就是一堆秒数:\n",os.path.getmtime('E:\Python_Learn'))
print("查看文件或文件夹的大小:\n",os.path.getsize('E:\Python_Learn'))
print("针对系统及文件类的操作".center(30,"+"))
print("查看当前路径: \n",os.getcwd())
print("查看当前路径下的所有文件: \n",os.listdir(os.getcwd())) #看来最后生成的结果是一个list
os.chdir('E:\\')#改变当前脚本工作目录
print("查看当前路径，结果一定会看到变成了E: \n",os.getcwd())
os.makedirs('dir1\dir2\dir3') #可生成多层递归目录
print("查看刚生成的递归目录",os.listdir('dir1'))
os.removedirs('dir1\dir2\dir3') #递归删除目录，dir2如果为空，则删掉，递归到dir2，如果为空，也删掉
os.mkdir('sigle_directory')#新建单级目录，而不是递归
print("确认刚刚创建的目录成功: \n",os.path.exists('E:\sigle_directory'))
os.rmdir('sigle_directory')
# os.rename('asdf.txt','gogogo.txt')
# os.remove('gogogo.txt') #删除一个文件
print("输出当前使用平台: \n",os.name)#win是nt，Linux是posix
print("输出操作系统特定的路径分隔符： \n",os.sep)
print("输出操作系统使用的行终止符： \n",os.linesep)
print("获取系统环境变量：\n",os.environ)#输出是一个元组里套字典
print("研究一下os下的walk方法".center(30,'+'))
y=os.walk('.')
for x,y,z in y:
#     print(i)
    print("dirpath,文件夹路径：",x)
    print("dirnames,文件夹名字：",y)
    print("filenames,文件名字：",z)

