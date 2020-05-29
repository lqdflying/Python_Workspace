# -*- coding:utf-8 -*-
###
# File: coroutine_simple.py
# Created Date: 2020-05-22
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday May 29th 2020 11:00:43 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

import asyncio
import time

async def say_after(delay, what):
    print(f"{what}: begin")
    await asyncio.sleep(delay)
    print(f"{what}: end")

async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())