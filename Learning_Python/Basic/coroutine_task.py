# -*- coding:utf-8 -*-
###
# File: coroutine_task.py
# Created Date: 2020-05-26
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 27th 2020 2:53:15 pm
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
strlist1 = ["ss","dd","gg"]
intlist1 = [1,2,5,6]
strlist2 = ["ss","dd","gg"]
intlist2 = [1,2,5,6]
c1 = mygen(strlist1)
c2 = mygen(intlist1)
c3 = mygen(strlist2)
c4 = mygen(intlist2)
print("生成的是一个协程对象",c1)

async def main():
    #串行
    await asyncio.create_task(c1)
    await asyncio.create_task(c2)
    #并行
    await asyncio.gather(
        c3,
        c4
    )

if __name__ == "__main__":
    asyncio.run(main())

'''
# 老式用法?
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(c1),
        asyncio.ensure_future(c2)
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished')
    loop.close()
'''