# -*- coding:utf-8 -*-
###
# File: coroutine_task.py
# Created Date: 2020-05-26
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Tuesday May 26th 2020 9:33:30 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import time,asyncio,random
async def mygen(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist)-1)
        print(alist.pop(c))
        await asyncio.sleep(1)
strlist = ["ss","dd","gg"]
intlist=[1,2,5,6]
c1=mygen(strlist)
c2=mygen(intlist)
print(c1)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(c1),
        asyncio.ensure_future(c2)
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished')
    loop.close()