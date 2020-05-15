# -*- coding:utf-8 -*-
###
# File: threading_queue.py
# Created Date: 2020-05-15
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday May 15th 2020 10:31:31 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import threading,time,random
import queue
food = queue.Queue()
def producer():
    """
    模拟生产者
    """
    for i in range(10):
        food.put("骨头 %s" % i)
    print("开始等待所有的骨头被取走...")
    food.join()  # 等待这个骨头队列被消费完毕
    print("所有的骨头被取完了...")
def consumer(name):
    """
    模拟消费者
    """
    i = 0
    while True:
        time.sleep(random.randrange(3))
        try:
            print("%s 取到"%name, food.get(block=False))
            # print("%s 取到"%name, food.get())
            food.task_done()  # 每去到一个骨头，便告知队列这个任务执行完了
            i += 1
        except queue.Empty:
            print("没有骨头了,%s共吃到%s根骨头"%(name,i))
            break


makebone = threading.Thread(target=producer,)
dog1 = threading.Thread(target=consumer, args=("qq",))
dog2 = threading.Thread(target=consumer, args=("aa",))
makebone.start()
dog1.start()
dog2.start()