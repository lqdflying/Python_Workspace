# -*- coding:utf-8 -*-
###
# File: multiprocessing_simple.py
# Created Date: 2020-05-17
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 20th 2020 3:28:29 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from multiprocessing import Process
import time,os
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

if __name__ == '__main__':
    # main_simple()
    main_inherit()

