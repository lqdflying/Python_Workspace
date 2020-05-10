# -*- coding:utf-8 -*-
###
# File: threading_simple.py
# Created Date: 2020-05-09
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday May 10th 2020 6:50:41 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import threading
import time


# print(type(threading.Thread))
def simple(num): #定义每个线程要运行的函数
   print("running on number:%s" %num)
   time.sleep(1)

class MyThread(threading.Thread):
   def __init__(self,num):
       threading.Thread.__init__(self)
       self.num = num
   def run(self):#定义每个线程要运行的函数
       print("running on number:%s"%self.num)
       time.sleep(1)       

def main_direct():
   t1 = threading.Thread(target=simple,args=(1,)) #生成一个线程实例,同时还传递了一个参数
   t2 = threading.Thread(target=simple,args=(2,)) #生成另一个线程实例,同时还传递了一个参数
   t1.start() #启动线程
   t2.start() #启动另一个线程
   print("直接调用".center(20,"+"))
   print(t1.getName()) #获取线程名
   print(t2.getName())

def main_inherit():
   t3 = MyThread(1)
   t4 = MyThread(2)
   print("继承式调用".center(20,"+"))
   t3.start()
   t4.start() 
   print(t3.getName()) #获取线程名
   print(t4.name)

def run_daemon(n):
   print('[%s]------running----' % n)
   time.sleep(1)
   print('%s号线程中实际有意义代码运行完了'%n)

def t_daemon():
   print("父线程会执行的代码")
   for i in range(5):
       t = threading.Thread(target=run_daemon,args=(i,))
       t.start()
       print('启动子线程->Name:%s,thread identifier:%s,native_id:%s'%(t.name,t.ident,t.native_id))
       t.join(1)

def main_daemon():
   m = threading.Thread(target=t_daemon,args=())
   m.setDaemon(True) #将main线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,由m启动的其它子线程会同时退出,不管是否执行完任务
   m.start()
   print("主线程的名字:%s"%m.name)
   m.join(timeout=3)
   # m.join()
   print("主线程停止".center(20,"="))

if __name__ == '__main__':
   # main_direct()
   # main_inherit()
   main_daemon()
