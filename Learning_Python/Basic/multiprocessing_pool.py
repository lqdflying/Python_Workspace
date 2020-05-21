# -*- coding:utf-8 -*-
###
# File: multiprocessing_pool.py
# Created Date: 2020-05-20
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Thursday May 21st 2020 2:19:34 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from multiprocessing import Queue, Process, Pool
import os,time,random
from collections import Counter

def before(name):
    print("启动进程池组{},当前子进程的PID是:{}".format(name,os.getpid()))

def apply_odd(i):
    print('执行apply_odd任务,传输的是奇数{0},它的进程pid是{1}'.format(i,os.getpid()))
    time.sleep(random.randrange(5))
    print('标号为{}的apply_odd任务执行完毕'.format(i))
    return os.getpid()

def apply_even(i):
    print('执行apply_even任务,传输的是偶数{0},它的进程pid是{1}'.format(i,os.getpid()))
    time.sleep(random.randrange(5))
    print('标号为{}的apply_even任务执行完毕'.format(i))
    return os.getpid()

def map_sample(i):
    print('第{0}次执map_async任务,它的进程pid是{1}'.format(i,os.getpid()))
    time.sleep(random.randrange(5))
    print('第{0}次执map_async任务执行完毕'.format(i))
    return os.getpid()

def map_start(name,age):
    print('用户{0},年龄{1}岁,它的进程pid是{2}'.format(name, age, os.getpid()))
    time.sleep(random.randrange(5))
    print('用户{0}任务执行完毕'.format(name))
    return os.getpid()

def setup_pool(n=5):
    apple_list = []
    map_list = []
    start_list = []
    user = [('liu', 12), ('anddy', 13)]
    p = Pool(processes=n, initializer=before, initargs=('Database',)) # 设置进程池的大小
    for i in range(10):
        if i%2 != 0:
            p.apply_async(apply_odd, args=(i,), callback=apple_list.append)
        elif i%2 == 0:
            p.apply_async(apply_even, args=(i,), callback=apple_list.append)
        else:
            continue
    p.map_async(map_sample, range(10), callback=map_list.append)
    p.starmap_async(map_start, user, callback=start_list.append)
    p.close() # 关闭进程池
    p.join()
    # for c in set(id_list): print("进程号为{}的一共被调用了{}次".format(c,id_list.count(c))) #写法一
    for m,n in Counter(apple_list).most_common(): print("apply_async函数:进程号为{}的一共被调用了{}次".format(m,n))  #写法二
    for m,n in Counter(map_list[0]).most_common(): print("map_list函数:进程号为{}的一共被调用了{}次".format(m,n))
    for m,n in Counter(start_list[0]).most_common(): print("start_list函数:进程号为{}的一共被调用了{}次".format(m,n))
    # print(map_list[0])
    print('主进程完成退出')


if __name__ == '__main__':
    setup_pool()  