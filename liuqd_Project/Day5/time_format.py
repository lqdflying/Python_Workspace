# -*- coding: utf-8 -*-
'''
Created on 2017年8月1日

@author: anddy.liu
'''

import time
x = time.time()
print("结构化数据→ 格式化输出：\n",time.strftime("%a,%A, %d %B %Y %H:%M:%S +0000",time.localtime())) #格式化输出只有%+后边的字符是固定格式的
print("格式化数据→ 结构化输出：\n",time.strptime("Tue,Tuesday, 01 August 2017 15:35:30 +0000", "%a,%A, %d %B %Y %H:%M:%S +0000"))
#print(time.strftime("%a,%A, %d %B %Y %H:%M:%S +0000",x)) #这样写会报错，Tuple or struct_time argument required
'''
%a    Locale’s abbreviated weekday name. 
%A    Locale’s full weekday name.
%b    Locale’s abbreviated month name.
%B    Locale’s full month name.
%c    Locale’s appropriate date and time representation.
%d    Day of the month as a decimal number [01,31].
%H    Hour (24-hour clock) as a decimal number [00,23].
%I    Hour (12-hour clock) as a decimal number [01,12].
%j    Day of the year as a decimal number [001,366].
%m    Month as a decimal number [01,12].
%M    Minute as a decimal number [00,59].
%p    Locale’s equivalent of either AM or PM.
%S    Second as a decimal number [00,61].
%U    Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0. 
%w    Weekday as a decimal number [0(Sunday),6].     
%W    Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0. 
%x    Locale’s appropriate date representation.
%X    Locale’s appropriate time representation.
%y    Year without century as a decimal number [00,99].
%Y    Year with century as a decimal number.
'''