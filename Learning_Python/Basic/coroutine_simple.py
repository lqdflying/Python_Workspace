# -*- coding:utf-8 -*-
###
# File: coroutine_simple.py
# Created Date: 2020-05-22
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 23rd 2020 10:49:51 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

import asyncio,random

async def iodemo(n):
    print("I/O模拟:开始处理%s,我会给它+1" %n)
    await asyncio.sleep(random.randrange(4))
    return n + 1


async def result(name):
    for i in range(5):
        result = await iodemo(i)
        print("[%s]: 处理后的值是%s" %(name,result) )
    return ("处理完了")

def get_result(corou):
    print("回调Calback:", corou.result())


loop = asyncio.get_event_loop()

print("start")

#第1种定义task的方法
loop_liu = result('liu')
# loop.run_until_complete(loop_liu)

# 第2种定义task的方法
quan = result('quan')
# loop_quan = loop.create_task(quan)
# loop.run_until_complete(loop_quan)

# 第3种定义task的方法
dong = result('dong')
# result_dong = asyncio.ensure_future(dong)
# result_dong.add_done_callback(get_result)

# loop.run_until_complete(result_dong)

# 多协程直接调用的方法
task = [
    asyncio.ensure_future(loop_liu),
    asyncio.ensure_future(quan),
    asyncio.ensure_future(dong)
]

loop.run_until_complete(asyncio.wait(task))
print("end")
loop.close()
