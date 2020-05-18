# -*- coding:utf-8 -*-
###
# File: multiprocessing_Gen_Process.py
# Created Date: 2020-05-18
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Monday May 18th 2020 5:15:15 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

import multiprocessing as mp
import os


#定义父进程变量
count = 1

# 定义子进程函数
def v():
    print('子进程:执行子进程,进程ID为:', os.getpid())
    print('子进程:当前模块名字为%s,进程ID为:'%__name__, os.getpid())
    print("子进程:如果子进程继承了__name__ == '__main__'中变化后的变量,则结果为2,反之为1:", count)


# 初始化语法
def init_func():
    print('初始化函数:当前生成进程的方式为:',mp.get_start_method())
    print('初始化函数:执行初始化,进程ID为:', os.getpid())
    print('初始化函数:当前模块名字为%s,进程ID为:'%__name__, os.getpid())
    

if __name__ == '__main__':
    init_func()
    count += 1 #父进程动态代码
    # start a new Process to execute function `v` and wait for it
    p = mp.Process(target=v)
    p.start()
    p.join()

#Linux下执行默认生成进程用fork(),输出结果为:
'''

当前生成进程的方式为: fork
执行初始化,进程ID为: 788
当前模块名字为__main__,进程ID为: 788
执行子进程,进程ID为: 789
当前模块名字为__main__,进程ID为: 789
如果执行了__name__ == '__main__'中变化后的变量,则结果为2,反之为1: 2
'''
#Windows下执行,默认生成进程用spawn(),输出结果为:
'''
当前生成进程的方式为: spawn
执行初始化,进程ID为: 14776
当前模块名字为__main__,进程ID为: 14776
执行子进程,进程ID为: 18448
当前模块名字为__mp_main__,进程ID为: 18448
如果子进程执行了__name__ == '__main__'中变化后的变量,则结果为2,反之为1: 1
'''