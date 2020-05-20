# -*- coding:utf-8 -*-
###
# File: multiprocessing_pool.py
# Created Date: 2020-05-20
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 20th 2020 11:20:37 pm
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

def before(name):
    print("启动进程池组{},当前子进程的PID是:{}".format(name,os.getpid()))

def test(i):
    print('第{0}次任务执行,它的进程pid是{1}'.format(i,os.getpid()))
    time.sleep(random.randrange(5))
    print('第{0}次任务执行完毕'.format(i))


def get_pool(n=5):
    p = Pool(processes=n, initializer=before, initargs=('Database',)) # 设置进程池的大小
    for i in range(10):
        p.apply_async(test,args=(i,))
    p.close() # 关闭进程池
    p.join()
    print('主进程完成退出')


if __name__ == '__main__':
    get_pool()  