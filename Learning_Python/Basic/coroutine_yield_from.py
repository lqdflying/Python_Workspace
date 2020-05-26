# -*- coding:utf-8 -*-
###
# File: coroutine_yield_from.py
# Created Date: 2020-05-26
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Tuesday May 26th 2020 4:16:48 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import asyncio,random
@asyncio.coroutine
def smart_fib(n): 
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 4)
        print("[Begin]: Smart one start to think for the {} time".format(b))
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('[End]: Smart one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        print("[Begin]: Stupid one start to think for the {} time".format(b))
        sleep_secs = random.uniform(0, 4)
        yield from asyncio.sleep(sleep_secs) #通常yield from后都是接的耗时操作
        print('[End]: Stupid one think {} secs to get {}'.format(sleep_secs, b))
        a, b = b, a + b
        index += 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        smart_fib(10),
        stupid_fib(10)
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()