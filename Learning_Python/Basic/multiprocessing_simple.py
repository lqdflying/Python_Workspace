# -*- coding:utf-8 -*-
###
# File: multiprocessing_simple.py
# Created Date: 2020-05-17
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 20th 2020 5:37:48 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from multiprocessing import Process
import time,os,random
def test():
    time.sleep(2)
    print('进程ID是: {}'.format(os.getpid()))

class MyProcess(Process):

    def run(self):
        time.sleep(2)
        print('子进程ID: {}'.format(os.getpid()))
        print('初始化函数:当前模块名字为%s,进程ID为:'%__name__, os.getpid())
    def __del__(self):
        print('执行__del__的进程ID: {}'.format(os.getpid()))

def main_simple():
    p = Process(target=test)
    p.start() # 子进程 开始执行
    p.join() # 等待子进程结束
    print('the process is ended')

def main_inherit():
    print('主进程的PID: {}'.format(os.getpid()))
    p = MyProcess()
    p.start()
    p.join()
    print('主进程停止')

def run_proc(name):
    print('子进程 {0} {1} 启动 '.format(name, os.getpid()))
    time.sleep(random.randrange(5))
    print('{}号子进程停止'.format(name))

def main_current():
    print('父进程 {0} 启动'.format(os.getpid()))
    process_list = []
    for i in range(5):
        p = Process(target=run_proc, args=(str(i),))
        # print('process start')
        p.start()
        process_list.append(p)
    for i in process_list: i.join()
    print('父进程退出')

if __name__ == '__main__':
    # main_simple()
    # main_inherit()
    main_current()

