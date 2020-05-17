# -*- coding:utf-8 -*-
###
# File: threading_queue_adv.py
# Created Date: 2020-05-15
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday May 17th 2020 6:10:10 pm
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
    while count < 15:
        time.sleep(random.randrange(3))
        baozi = '%s-%s'%(name,count)
        food.put(baozi)  # 在队列里放包子
        print('工人 %s 生产了名为 %s 的包子并放在了盘子里.' % (name, baozi))
        count += 1
'''
#第1种消费者使用count来终止while循环
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
'''
def consumer(name):
#第2种消费者使用try+except来终止循环
    count = 0
    while True:
        time.sleep(random.randrange(4))
        try:
            data = food.get(timeout=6)  # 就继续获取包子
            print('\033[32;1m顾客 %s 吃掉了盘子里编号为 %s 的包子...\033[0m' % (name, data))
            count += 1
        except queue.Empty:
            print("盘子里没有包子了,顾客%s一共抢到了%s个包子"%(name, count))
            break
p1 = threading.Thread(target=producer, args=('Anddy',))
p2 = threading.Thread(target=producer, args=('Jimmy',))
c1 = threading.Thread(target=consumer, args=('Tom',))
c2 = threading.Thread(target=consumer, args=('Jaccob',))
#当前py文件运行的时候会同时生成4个线程,2个生产者线程,2个消费者线程,
#他们之间,彼此没有先后关系,仅使用queue.Queue()来处理并协作作问题
p1.start()
p2.start()
c1.start()
c2.start()