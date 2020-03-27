# -*- coding: utf-8 -*-
'''
Created on 2017年8月3日

@author: anddy.liu
'''
import shutil
#将一个文件中的内容拷贝到另一个文件，可以部分内容，具体部分内容是多少就用这个shutil.copyfileobj(fsrc, fdst[, length])的第三个参数length来定
with open("liuqdnew", "r",  encoding = "utf-8") as liuqdfile:
    with open("liuqd1.json", "w",  encoding = "utf-8") as liuqd1:
        shutil.copyfileobj(liuqdfile,liuqd1)
#直接使用名字就实现了将一个文件copy成一份新生成另一个文件。shutil.copyfile(src, dst)的函数本身就自动加上了with open的功能
#shutil.copyfile("liuqdnew","liuqdnew1")
# shutil.copymode(src, dst)  #仅拷贝权限。内容、组、用户均不变
#shutil.copystat(src, dst) #Copy all stat info (mode bits, atime, mtime, flags) from src to dst.#拷贝状态的信息，包括：mode bits, atime, mtime, flags
#shutil.copy(src, dst) #拷贝文件和权限，这个函数了先引用了copyfile，又引用了copymode
#shutil.copy2(src, dst) #拷贝文件和权限，这个函数了先引用了copyfile，又引用了copystat
#shutil.copytree("module1","new_mode",ignore=shutil.ignore_patterns("*init*",'*.pyc', 'tmp*')) 
#递归的去拷贝文件，实际上是copy目录,这里的ignore=shutil.ignore_patterns("*init*",'*.pyc', 'tmp*')是用来忽略部分文件
#shutil.rmtree(path[, ignore_errors[, onerror]]) #删除目录
#shutil.move(src, dst) 
'''
Recursively move a file or directory to another location. 
This is similar to the Unix "mv" command. Return the file or directory's destination.
'''

#最后一个压缩和打包
'''
shutil.make_archive(base_name, format,...)

创建压缩包并返回文件路径，例如：zip、tar

base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
如：www                        =>保存至当前路径
如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
format：    压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir：    要压缩的文件夹路径（默认当前目录）
owner：    用户，默认当前用户
group：    组，默认当前组
logger：    用于记录日志，通常是logging.Logger对象
#####以下是示例#######
#将 /Users/wupeiqi/Downloads/test 下的文件打包放置当前程序目录
 
import shutil
ret = shutil.make_archive("wwwwwwwwww", 'gztar', root_dir='/Users/wupeiqi/Downloads/test')
 
 
#将 /Users/wupeiqi/Downloads/test 下的文件打包放置 /Users/wupeiqi/目录
import shutil
ret = shutil.make_archive("/Users/wupeiqi/wwwwwwwwww", 'gztar', root_dir='/Users/wupeiqi/Downloads/test')
'''

