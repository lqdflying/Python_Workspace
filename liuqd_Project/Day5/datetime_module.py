# -*- coding: utf-8 -*-
'''
Created on 2017年8月1日

@author: anddy.liu
'''
import datetime
print("获取当前时间：\n",datetime.datetime.now(),type(datetime.datetime.now()))
print("获取当前三天前的时间：\n",datetime.datetime.now()+datetime.timedelta(days = -3))
print("获取三天后的时间：\n",datetime.datetime.now()+datetime.timedelta(days = 3))
print("获取三小时前的时间：\n",datetime.datetime.now()+datetime.timedelta(hours = -3))
print("获取三小时后的时间：\n",datetime.datetime.now()+datetime.timedelta(hours = 3))
year = datetime.timedelta(days=365)
print(type(year))
#class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)