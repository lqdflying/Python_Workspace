# -*- coding: utf-8 -*-
'''
Created on 2017年7月9日

@author: anddy.liu
'''
#f = open("liuqdarticle.txt","r",encoding = "utf-8")
#这里就是和pycharm不一样的地方，pydev更加严谨，如果不是使用with open的方式打开一个文件，那么文件变量输入点号之后甚至不会给你各种method的提示

'''
with open("liuqdarticle.txt","r",encoding = "utf-8") as liuqdfile:  #这里的r是默认的，默认不写也是r，但是想写的话，则需要w
    print(liuqdfile.read())
    print("再执行一次".center(50,"+"))
    print("\n")
    print(liuqdfile.read())  #因为第一次read()已经在文件末尾了，所以这里会什么都print不出来

with open("liuqdarticle.txt","w",encoding = "utf-8") as liuqdfile:  #注意，这种w的方式实际上等于创建一个文件，原来的东西会被覆盖掉
    liuqdfile.write("再写一行")
#   print(liuqdfile.read())  #这一行其实无法执行，因为在w模式下无法read

with open("liuqdarticle.txt","r",encoding = "utf-8") as liuqdfile:
    print(liuqdfile.read())
 
with open("liuqdarticle.txt","a",encoding = "utf-8") as liuqdfile:  
#注意，如果是追加，那么需要使用a的方式打开文件,也就是append，但是append的方式依然不能行写
    liuqdfile.write("\n天安门上太阳升")
#    print(liuqdfile.read())  #有这一行会报错

with open("liuqdarticle.txt","r",encoding = "utf-8") as liuqdfile:  
#如果是a+，则是可以执行read()方法的
    #liuqdfile.write("\n天安门上太阳升")
    #print(liuqdfile.read()) #第一次执行是去取并打印全部文件
    #print(liuqdfile.read()) #第二次因为read方法的指正已经到了末尾，那么就什么都没有了，因此，需要将指针回到开头，方法如下
    #下班就是方法：
    print(liuqdfile.readline())
    print(liuqdfile.readline())
    print(liuqdfile.readline())
    print(liuqdfile.tell())  #打印当前字符位置
    liuqdfile.seek(0)  #回到最开始
    print(liuqdfile.readline())  #这里就是重新打印第一行  
    print(liuqdfile.encoding)    #返回打开文件的编码格式
    print(liuqdfile.fileno())    #返回文件句柄在内存中的编号
    #liuqdfile.flush()   #刷新文件缓存的到硬盘上

with open("liuqdarticle.txt","a",encoding = "utf-8") as liuqdfile:
    liuqdfile.truncate(10) #截断文件，不指定是从0截断， 指定就是从指定字符位置截断，也可以使用seek方法先skip到某个字符位置，再truncate


with open("liuqdarticle.txt","r",encoding = "utf-8") as liuqdfile:
    for i in range(10):
        f = liuqdfile.readline()
        while i >=5:
            print(f)
            break  #这是读5-10行的写法，需要用while写个判断,break是跳出while循环，其实这里if会比较好

print("分割线".center(50,"+"))
with open("liuqdarticle.txt","r",encoding = "utf-8") as liuqdfile:
    for index,line in enumerate(liuqdfile.readlines()): #readlines这里会把文件的每一行组成一个list（列表），每行一个元素,这个是把整个文件读取到内存里
        print(index,line.strip())  #使用strip去掉空行和空格

#以上是low写法，会把所有数据载入内存

#以下是比较高级的写法
with open("liuqdarticle.txt","r",encoding = "utf-8") as liuqdfile:
    count = 1
    for line in liuqdfile:  #之所以这里比较高级，是因为这里的liuqdfile已经不是list了，而是变成了迭代器
        if  count ==9 :
            print("第九行省略".center(50,"+"))
            count +=1
            continue
        print(count,"-->",line.strip())
        count +=1
'''       
with open("liuqdfile.txt","a+",encoding = "utf-8") as mynewfile:
    mynewfile.write("写一行\n")
#   mynewfile.flush()
    mynewfile.seek(0)  #看来必须要flush，只需要把文件回到行首，也就是seek(0)，就可以实现写一行，就正确的打印一行
    print(mynewfile.read())

