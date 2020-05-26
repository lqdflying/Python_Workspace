# -*- coding:utf-8 -*-
###
# File: coroutine_adv.py
# Created Date: 2020-05-26
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Tuesday May 26th 2020 11:04:21 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
# python协程只能运行在事件循环中，但是一旦事件循环运行，又会阻塞当前任务。所以只能在当前进程中再开一个线程，这个线程的主要任务是运行事件循环，
# 就是event_loop,因为他是一个无限循环，会阻塞当前线程。放一个自己写的demo，注释写的很详细。另外还有一点需要注意，一个事件循环中不能运行另外一个事件循环。
import asyncio
from threading import Thread
  
  
async def production_task():
    i = 0
    while True:
        # 将consumption这个协程每秒注册一个到运行在线程中的循环，thread_loop每秒会获得一个一直打印i的无限循环任务
        asyncio.run_coroutine_threadsafe(consumption(i),
                                         thread_loop)  # 注意：run_coroutine_threadsafe 这个方法只能用在运行在线程中的循环事件使用
        await asyncio.sleep(1)  # 必须加await
        i += 1
  
  
async def consumption(i):
    while True:
        print("我是第{}任务".format(i))
        await asyncio.sleep(1)
  
  
def start_loop(loop):
    #  运行事件循环， loop以参数的形式传递进来运行
    asyncio.set_event_loop(loop)
    loop.run_forever()
  
  
thread_loop = asyncio.new_event_loop()  # 获取一个事件循环
run_loop_thread = Thread(target=start_loop, args=(thread_loop,))  # 将次事件循环运行在一个线程中，防止阻塞当前主线程
run_loop_thread.start()  # 运行线程，同时协程事件循环也会运行
  
advocate_loop = asyncio.get_event_loop()  # 将生产任务的协程注册到这个循环中
advocate_loop.run_until_complete(production_task())  # 运行次循环