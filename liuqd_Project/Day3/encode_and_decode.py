# -*- coding: utf-8 -*-
'''
Created on 2017年7月11日

@author: anddy.liu
'''
s = "你好" #python默认的变量是以Unicode编码的，文件头的声明仅仅是说整个代码以utf-8展示
#s.decode()  #因为已经是Unicode了，所以这里没有decode整个方法
print("utf-8是Unicode的扩展集，即便是utf-8的terminal，但是Unicode编码的可以直接打印：-->\n",s)
s_encode = s.encode(encoding='gbk', errors='strict')  #以GBK编码
print("将一个Unicode编码的文件以gbk编码，这里显示的是源码：-->\n",s_encode)
print("将一个gbk编码的文件以gbk解码，这里显示的是源码解码后对应的中文：-->\n",s_encode.decode("gbk"))

s_encode = s.encode(encoding='utf-8', errors='strict') #以UTF-8编码
print("将一个Unicode编码的文件以utf-8编码，这里显示的是源码：-->\n",s_encode)
print("将一个utf-8编码的文件以gbk解码，这里显示的是源码解码后对应的中文(当然，肯定是乱码)：-->\n",s_encode.decode("gbk"))
print("将一个utf-8编码的文件以utf-8解码，这里显示的是源码解码后对应的中文(这里才是正常的)：-->\n",s_encode.decode("utf-8"))