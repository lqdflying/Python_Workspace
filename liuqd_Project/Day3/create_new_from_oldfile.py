# -*- coding: utf-8 -*-
'''
Created on 2017年7月11日

@author: anddy.liu
'''
'''
f = open("liuqdarticle.txt","r",encoding = "utf-8")

fnew = open("liuqdnew",'w',encoding = "utf-8")

for line in f:
    if "肆意的快乐" in line:
        line = line.replace("肆意的快乐","+++++肆意的快乐++++")
        fnew.write(line)
    else:
        fnew.write(line)

f.close()
fnew.close()

#以上是老师的讲法，但是pydev下没有方法提示，也许pycharm下有,我发现文件处理这块，pydev的提示总不是很好
'''
with open("liuqdarticle.txt","r",encoding = "utf-8") as f , \
open("liuqdnew",'w',encoding = "utf-8") as fnew:   #python官方推荐一行代码不要超过80个字符，使用\实现代码换行解析上算一行 
    for line in f:
        if "肆意的快乐" in line:
            line = line.replace("肆意的快乐","+++++肆意的快乐++++")
            fnew.write(line)
        else:
            fnew.write(line)