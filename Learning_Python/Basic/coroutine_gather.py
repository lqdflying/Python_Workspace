# -*- coding:utf-8 -*-
###
# File: coroutine_gather.py
# Created Date: 2020-05-29
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday May 29th 2020 11:33:22 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

import time,asyncio,random

async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"任务{name}: 计算阶乘({number})中...")
        await asyncio.sleep(1)
        f *= i
    print(f"任务 {name}: 阶乘({number}) = {f}")

async def main():
    # Schedule three calls *concurrently*:
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )

if __name__ == "__main__":
    asyncio.run(main())

