# -*- coding:utf-8 -*-
###
# File: multiprocessing_lock.py
# Created Date: 2020-05-21
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Thursday May 21st 2020 5:48:18 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from multiprocessing import Pool, Lock
import os,random,time
muex = Lock()

def test(i):
    time.sleep(random.randrange(4))
    muex.acquire()
    print('{}进程正在写入'.format(os.getpid()))
    with open('%s/test_pro.txt'%os.path.dirname(__file__), 'a+', encoding='utf-8') as f:
        f.write(str(i)+'\n')
    muex.release()

if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        p.apply_async(test, args=(i,))
    p.close()
    p.join()
    with open('%s/test_pro.txt'%os.path.dirname(__file__), 'r+', encoding='utf-8') as f:
        print(f.read())