# -*- coding:utf-8 -*-
###
# File: coroutine_run.py
# Created Date: 2020-05-27
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 27th 2020 3:37:38 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import asyncio
from threading import Thread

def start_thread_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

async def thread_example(name):
    print('正在执行name:', name)
    await asyncio.sleep(1)
    return '返回结果：' + name

new_loop = asyncio.new_event_loop()
t = Thread(target= start_thread_loop, args=(new_loop,))
t.start()

future = asyncio.run_coroutine_threadsafe(thread_example('Zarten1'), new_loop)
print(future.result())

asyncio.run_coroutine_threadsafe(thread_example('Zarten2'), new_loop)

print('主线程不会阻塞')

asyncio.run_coroutine_threadsafe(thread_example('Zarten3'), new_loop)

print('继续运行中...')