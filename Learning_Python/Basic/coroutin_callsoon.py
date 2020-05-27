# -*- coding:utf-8 -*-
###
# File: coroutin_callsoon.py
# Created Date: 2020-05-27
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 27th 2020 3:37:08 pm
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

def thread_example(name):
    print('正在执行name:', name)
    return '返回结果：' + name

new_loop = asyncio.new_event_loop()
t = Thread(target= start_thread_loop, args=(new_loop,))
t.start()

handle = new_loop.call_soon_threadsafe(thread_example, 'Zarten1')
handle.cancel()

new_loop.call_soon_threadsafe(thread_example, 'Zarten2')

print('主线程不会阻塞')

new_loop.call_soon_threadsafe(thread_example, 'Zarten3')

print('继续运行中...')
# new_loop.close()