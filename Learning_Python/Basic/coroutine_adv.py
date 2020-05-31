# -*- coding:utf-8 -*-
###
# File: coroutine_adv.py
# Created Date: 2020-05-26
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday May 31st 2020 3:38:58 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import asyncio,time
from threading import Thread

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def stop_loop():
    # event loop监控协程,目的是如果当前 event loop为空,则退出
    while True:
        if len(asyncio.all_tasks()) != 1:
            print(f"当前event loop共有{len(asyncio.all_tasks())}个task在运行",)
            await asyncio.sleep(3) #每3秒钟扫一遍当前的event loop,看看有几个任务
            continue
        else:
            print("没有多于的task了,关闭整个事件循环")
            break
    a = asyncio.get_running_loop()
    # print(a)
    a.stop()

async def cancel_me():
    print(f"cancel_me(): before sleep at {time.strftime('%X')}")

    try:
        # Wait for 1 hour
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print(f"cancel_me(): cancel sleep at {time.strftime('%X')}")
        raise
    finally:
        print(f"cancel_me(): after sleep at {time.strftime('%X')}")

async def cancel_main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())
    print(f"返回task的名字at {time.strftime('%X')}: ",task.get_name())
    # Wait for 1 second
    await asyncio.sleep(5)
    
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(f"main(): cancel_me is cancelled now at {time.strftime('%X')}")



new_loop = asyncio.new_event_loop()
t_run = Thread(target=start_loop, args=(new_loop,))
t_run.start()

for i in range(2):#协程开启十个
    asyncio.run_coroutine_threadsafe(cancel_main(), new_loop)

asyncio.run_coroutine_threadsafe(stop_loop(), new_loop)