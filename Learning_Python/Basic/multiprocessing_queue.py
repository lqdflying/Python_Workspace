# -*- coding:utf-8 -*-
###
# File: multiprocessing_queue.py
# Created Date: 2020-05-22
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday May 22nd 2020 1:42:30 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from multiprocessing import Process, Pool, Queue, Manager
import time,random
import queue #单纯从multiprocessing里引入Queue并不能cache queue.Empty异常,还得import queue
    

def customer (name,food):
    while True:
        try:
            data = food.get(timeout=7)
            print('{}吃到了食物:{}'.format(name, data))
            # print(f"{name}吃到了食物{food.get(timeout=7)}")
            time.sleep(random.randrange(3))
        except queue.Empty:
            print(f"{name}没有食物吃了")
            break

def producer (name,food,foodtype,n):
    i = 1
    while i <= n:
        print(f"{name}做了食物:{foodtype}-{i}")
        food.put(f"{foodtype}-{i}")
        time.sleep(random.randrange(3))
        i += 1

def dinner_Process(foodlist,cus_list):
    cooker = ['Tom', 'Anddy', 'Boom', 'justin', 'jimmy']
    food = Queue()

    p_list = []
    for m,n in zip(foodlist,cooker):
        p = Process(target=producer, args=(n, food, m, 5))
        p.start()
        p_list.append(p)
    for i in cus_list:
        p = Process(target=customer, args=(i, food)) 
        p.start()
        p_list.append(p)
    for i in p_list: i.join()

    print("吃饭完毕")


def dinner_Manager(foodlist,cus_list):
    cooker = ['Tom', 'Anddy', 'Boom', 'justin', 'jimmy']
    m = Manager()
    food = m.Queue()
    p = Pool(processes=10)
    for m,n in zip(foodlist,cooker):
        p.apply_async(producer, args=(n, food, m, 5))
    for i in cus_list:
        p.apply_async(customer, args=(i, food))
    p.close()
    p.join()

    print("吃饭完毕")

if __name__ == "__main__":
    foodlist = ['馒头', '花卷', '大饼']
    cus_list = ['小明', "小王", "小强", "小刘"]
    dinner_Process(foodlist, cus_list)
    # dinner_Manager(foodlist, cus_list)