# -*- coding:utf-8 -*-
###
# File: multiprocessing_queue_test.py
# Created Date: 2020-05-22
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday May 22nd 2020 1:06:13 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from multiprocessing import Process, Queue, Pool
def writer(i,q):
    message = f'I am Process {i}'
    q.put(message)
def reader(i,q):
    message = q.get()
    print(message)
if __name__ == '__main__':
    # Create multiprocessing queue
    q = Queue()
    # Create a group of parallel writers and start them
    for i in range(10):
        Process(target=writer, args=(i,q,)).start()
    # Create multiprocessing pool
    p = Pool(10)
    # Create a group of parallel readers and start them
    # Number of readers is matching the number of writers
    # However, the number of simultaneously running
    # readers is constrained to the pool size
    readers = []
    for i in range(10):
        readers.append(p.apply_async(reader, (i,q,)))
    # Wait for the asynchrounous reader threads to finish
    [r.get() for r in readers]