# -*- coding: utf-8 -*-
'''
Created on 2018年3月2日

@author: anddy.liu
'''
import time
import datetime

print("返回处理器时间：：\n",time.clock())
print("返回与utc时间的时间差，以秒计算：：\n",time.altzone)
print("使用asctime，返回字符串格式的时间：\n",time.asctime())
print("使用ctime返回字符串格式的时间：\n",time.ctime())
print("元组类型时间的时间的转换".center(30,"+"))
x=time.localtime()#x就是一个元组，并且是当时时间
print("以元组方式返回本地当地时间：\n",type(x),"----格式是元组\n",x)
print("元组时间转换为字符串格式：\n",time.asctime(x))
print("元组时间转换为时间戳：\n",time.mktime(x))
print("时间戳类型时间的转换".center(30,"+"))
y=time.mktime(time.localtime())#y是一个时间戳
print("这是一个时间戳：\n",type(y),"----格式是浮点数\n",y)
print("将浮点数的时间戳转换为字符串：\n",time.ctime(y))
z=time.asctime() #这是一个字符串格式的时间
print("字符串类型时间的转换".center(30,"+"))
print("字符串类型转换成元组：\n",time.strptime(z))
print("开始演示datetime函数".center(30,"+"))
print("返回当前时间: \n",datetime.datetime.now())
print("之前定义的时间戳直接转换成日期格式：\n",datetime.date.fromtimestamp(y))
print("之前定义的时间戳直接转换成日期+时间格式：\n",datetime.datetime.fromtimestamp(y))
print("当前时间+3天：\n",datetime.datetime.now() + datetime.timedelta(3))
print("当前时间-3天：\n",datetime.datetime.now() + datetime.timedelta(-3))
print("当前时间+3小时：\n",datetime.datetime.now() + datetime.timedelta(hours=3))
print("当前时间+30分：\n",datetime.datetime.now() + datetime.timedelta(minutes=30))
print("当前日期+3天(注意，仅仅是日期，而不是日期带时间)：\n",datetime.date.today()+datetime.timedelta(3))
print("当前日期-3天(注意，仅仅是日期，而不是日期带时间)：\n",datetime.date.today()+datetime.timedelta(-3))