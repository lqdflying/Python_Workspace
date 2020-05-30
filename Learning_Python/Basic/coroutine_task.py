# -*- coding:utf-8 -*-
###
# File: coroutine_task.py
# Created Date: 2020-05-30
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 30th 2020 9:44:25 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import asyncio,time
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

async def main():
    # Create a "cancel_me" Task
    task = asyncio.create_task(cancel_me())
    print(f"返回task的名字at {time.strftime('%X')}: ",task.get_name())
    # Wait for 1 second
    await asyncio.sleep(5)
    print(asyncio.all_tasks())
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(f"main(): cancel_me is cancelled now at {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main())
    
'''
1. "await asyncio.sleep(5)"会让协程main()协程挂起,event loop会继续执行"await task",然后协程cancel_me()至少会被__next__()一次,也就是会走到"await asyncio.sleep(3600)"这里然后挂起(之前会print一个"before sleep")
2. cancel_me()挂起后(这个挂起设置了3600秒,所以他铁得等),event loop转而寻找loop其他先"挂起结束"的协程,这里就是main()了,因为"await asyncio.sleep(5)"5秒后就会到期← 注意这里就有一个5秒的时间段
3. 一瞬间,同一时间,event loop由于"task.cancel()"的存在,在处理完main()里的await后就转而抛出一个CancelledError异常给"cancel_me()"[a CancelledError exception to be thrown into the wrapped coroutine on the next cycle of the event loop],然后协程cancel_me()里的"await asyncio.sleep(3600)"就不会继续等待下去了
4. 一瞬间,同一时间,"cancel sleep","after sleep","main()三个输出同时发生了"
[输出:]
cancel_me(): before sleep at 21:11:26
cancel_me(): cancel sleep at 21:11:31
cancel_me(): after sleep at 21:11:31
main(): cancel_me is cancelled now at 21:11:31
'''