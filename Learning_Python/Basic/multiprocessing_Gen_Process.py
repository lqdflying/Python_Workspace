# -*- coding:utf-8 -*-
###
# File: multiprocessing_Gen_Process.py
# Created Date: 2020-05-18
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 20th 2020 3:33:31 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

import multiprocessing as mp
import os,time


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


class MyProcess(mp.Process): #这里还非得是大写,如果写成是mp.process会报错:"Inheriting 'mp.process', which is not a class"

    def run(self):
        time.sleep(2)
        print('子进程ID: {}'.format(os.getpid()))
        print('初始化函数:当前模块名字为%s,进程ID为:'%__name__, os.getpid())
    def __del__(self):
        print('执行__del__的进程ID: {}'.format(os.getpid()))
    
def main_simple():
    init_func()
    # start a new Process to execute function `v` and wait for it
    p = mp.Process(target=v)
    p.start()
    p.join()

def main_inherit():
    print('主进程的PID: {}'.format(os.getpid()))
    p = MyProcess()
    p.start()
    p.join()
    print('主进程停止')
    

if __name__ == '__main__':
    print("简单process实验".center(20,"+"))
    count += 1 #父进程动态代码
    main_simple()
    print("\n")
    print("process派生类实验".center(20,"+"))
    main_inherit()


#Linux下执行默认生成进程用fork(),输出结果为:
'''
++++简单process实验+++++
初始化函数:当前生成进程的方式为: fork
初始化函数:执行初始化,进程ID为: 1106
初始化函数:当前模块名字为__main__,进程ID为: 1106
子进程:执行子进程,进程ID为: 1107
子进程:当前模块名字为__main__,进程ID为: 1107
子进程:如果子进程继承了__name__ == '__main__'中变化后的变量,则结果为2,反之为1: 2


++++process派生类实验++++
主进程的PID: 1106
子进程ID: 1108
初始化函数:当前模块名字为__main__,进程ID为: 1108
主进程停止
执行__del__的进程ID: 1106
'''
#Windows下执行,默认生成进程用spawn(),输出结果为:
'''
++++简单process实验+++++
初始化函数:当前生成进程的方式为: spawn
初始化函数:执行初始化,进程ID为: 14736
初始化函数:当前模块名字为__main__,进程ID为: 14736
子进程:执行子进程,进程ID为: 24248
子进程:当前模块名字为__mp_main__,进程ID为: 24248
子进程:如果子进程继承了__name__ == '__main__'中变化后的变量,则结果为2,反之为1: 1


++++process派生类实验++++
主进程的PID: 14736
子进程ID: 20920
初始化函数:当前模块名字为__mp_main__,进程ID为: 20920
执行__del__的进程ID: 20920
主进程停止
执行__del__的进程ID: 14736

'''