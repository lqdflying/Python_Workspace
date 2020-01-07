# -*- coding: utf-8 -*-
'''
Created on 2017年7月28日

@author: anddy.liu
'''
import time

x = time.time() #获取一个时间戳，这里得出的是秒，所以得换算
print(x/3600/24/365+1970)#这里就是粗略的换算成年
print("数据类型：\n",type(time.localtime()),"\n具体数据：\n",time.localtime()) #tm_wday=4，从0开始，0是周一，4就是周五
print("时区：",time.timezone)  #-28800就是-8.就是早8小时，就是东八区
print("UAT时间和夏令时的差时：",time.timezone)  #-28800就是-8.就是早8小时，就是东八区
print("time模块的方法：".center(50,"+"))
time.sleep(2) #睡几秒
print("UTC时间",time.gmtime())  #传入的是秒，换算成年月日时分秒周的元组格式输出，但是要注意，这里输出的是UTC时间，如果什么都不穿入，那么就是引入time.time()的值
print("本地时区时间",time.localtime()) #传入的是秒，换算成年月日时分秒周的元组格式输出，但是要注意，这里输出的是本地时间，如果什么都不穿入，那么就是引入time.time()的值
print("我要取出来时间：".center(50,"+"))
print("本地时区时间,我要单独取出来年:",time.localtime().tm_year) #year, for example, 1993
print("本地时区时间,我要单独取出来月:",time.localtime().tm_mon) #month of year, range [1, 12]
print("本地时区时间,我要单独取出来日:",time.localtime().tm_mday) #day of month, range [1, 31]
print("本地时区时间,我要单独取出来时:",time.localtime().tm_hour) #hours, range [0, 23]
print("本地时区时间,我要单独取出来分:",time.localtime().tm_min) #minutes, range [0, 59]
print("本地时区时间,我要单独取出来秒:",time.localtime().tm_sec) #seconds, range [0, 61])
print("本地时区时间,我要单独取出来yday:",time.localtime().tm_yday) #day of year, range [1, 366]
print("本地时区时间,我要单独取出来wday:",time.localtime().tm_wday) #day of week, range [0, 6], Monday is 0
print("本地时区时间,我要单独取出来年，随便找出来一年",time.localtime(1231445311).tm_year) 
print("本地时区时间,mktime的用法:",time.mktime(time.localtime())) # Convert a time tuple in local time to seconds since the Epoch
