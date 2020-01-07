# -*- coding: utf-8 -*-
'''
Created on 2017年7月11日

@author: anddy.liu
'''
import time
def logger(logthing):
    time_format = "%Y-%m-%d %X"
    time_current = time.strftime(time_format)
    with open("logger.txt","a+",encoding = "utf-8") as log:
#       log.write(time_current+"--->"+logthing)  #第一种在字符串中拼接变量的方式
        log.write("{_time_current} ----> {_logthing}".format(_time_current = time_current, _logthing = logthing))
        #第二种在字符串中拼接变量的方式，我觉得第二种好用且正规一点
        return True


x = logger("第1行\n")
y = logger("第2行\n")   
z = logger("第3行\n")
print(x)
print(y)
print(z)