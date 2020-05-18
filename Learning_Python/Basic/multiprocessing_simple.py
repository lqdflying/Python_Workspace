# -*- coding:utf-8 -*-
###
# File: multiprocessing_simple.py
# Created Date: 2020-05-17
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Monday May 18th 2020 4:25:37 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from multiprocessing import Queue, Process
import time,os
def test():
    time.sleep(2)
    print('进程ID是: {}'.format(os.getpid()))

class MyProcess(Process):

    def run(self):
        time.sleep(2)
        print('this is process {}'.format(os.getpid()))

    def __del__(self):
        print('del the process {}'.format(os.getpid()))

def main_simple():
    p = Process(target=test)
    p.start() # 子进程 开始执行
    p.join() # 等待子进程结束
    print('the process is ended')

def main_inherit():
    p = MyProcess()
    p.start()
    p.join()
    print('ths process is ended')

if __name__ == '__main__':
    # main_simple()
    main_inherit()

