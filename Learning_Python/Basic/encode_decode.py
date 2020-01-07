# -*- coding: utf-8 -*-
'''
Created on 2017年8月22日

@author: anddy.liu
'''
a='我很好' ####python3 默认的编码为unicode
###unicode>gb2312
unicode_gb2312=a.encode('gb2312') 
###因为默认是unicode所以不需要decode()，直接encode成想要转换的编码如gb2312
print('我的gb2312',unicode_gb2312)
###gb2312>utf8
gb2312_utf8=unicode_gb2312.decode('gb2312').encode('utf-8') 
##当前字符为gb2312所以要先decode成unicode(decode中传入的参数为当前字符的编码集)然后再encode成utf-8
print('我是utf-8',gb2312_utf8) 
###utf8>gbk
utf8_gbk=gb2312_utf8.decode('utf-8').encode('gbk')
##当前字符集编码为utf-8要想转换成gbk先decode成unicode字符集再encode成gbk字符集
print("我是gbk",utf8_gbk) 
###utf8>uicode
utf8_unicode=utf8_gbk.decode('gbk') 
####注意当转换成unicode时 并不需要encode()
print('我是unicode',utf8_unicode) 
###unicode>gb18030
unicode_gb18030=utf8_unicode.encode('gb18030')
print('我是gb18030',unicode_gb18030) 

print("各种编码转换".center(50,"+"))
s = "你好" #python默认的变量是以Unicode编码的，文件头的声明仅仅是说整个代码以utf-8展示
#s.decode()  #因为已经是Unicode了，所以这里没有decode这个方法
print("utf-8是Unicode的扩展集，即便是utf-8的terminal，但是Unicode编码的可以直接打印：-->\n",s)
s_encode = s.encode(encoding='gbk', errors='strict')  #以GBK编码
print("将一个Unicode编码的文件以gbk编码，这里显示的是源码：-->\n",s_encode)
print("将一个gbk编码的文件以gbk解码，这里显示的是源码解码后对应的中文：-->\n",s_encode.decode("gbk"))

s_encode = s.encode(encoding='utf-8', errors='strict') #以UTF-8编码
print("将一个Unicode编码的文件以utf-8编码，这里显示的是源码：-->\n",s_encode)
print("将一个utf-8编码的文件以gbk解码，这里显示的是源码解码后对应的中文(当然，肯定是乱码)：-->\n",s_encode.decode("gbk"))
print("将一个utf-8编码的文件以utf-8解码，这里显示的是源码解码后对应的中文(这里才是正常的)：-->\n",s_encode.decode("utf-8"))