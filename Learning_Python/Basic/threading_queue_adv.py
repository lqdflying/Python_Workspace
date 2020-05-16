# -*- coding:utf-8 -*-
###
# File: threading_queue_adv.py
# Created Date: 2020-05-15
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 16th 2020 10:20:45 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import time,random
import queue,threading
food = queue.Queue()
def producer(name):
    count = 0
    while count < 30:
        time.sleep(random.randrange(3))
        food.put(count)  # 在队列里放包子
        print('工人 %s 生产了 %s 号包子并放在了盘子里.' % (name, count))
        count += 1
def consumer(name):
    count = 0
    while count < 20:
        time.sleep(random.randrange(4))
        if not food.empty():  # 如果还有包子
            data = food.get()  # 就继续获取包子
            # print(data)
            print('\033[32;1m顾客 %s 吃掉了盘子里编号为 %s 的包子...\033[0m' % (name, data))
        else:
            print("-----盘子里没有包子了----")
        count += 1
p1 = threading.Thread(target=producer, args=('Anddy',))
c1 = threading.Thread(target=consumer, args=('Tom',))
c2 = threading.Thread(target=consumer, args=('Jaccob',))
#当前py文件运行的时候会同时生成3个线程,1个生产者线程,2个消费者线程,
#他们之间,彼此没有先后关系,仅使用queue.Queue()来处理并协作作问题
p1.start()
c1.start()
c2.start()