# -*- coding:utf-8 -*-
###
# File: product_customer_example1.py
# Created Date: 2020-05-15
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday May 15th 2020 3:19:23 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
#生产者和消费者，使用生成器的方式，就是一个简单的并行，
import time
def customer(name):
    print('%s开始吃包子了'%name) #打印出对应的消费者的名字
    while True: #执行一个死循环 实际上就是需要调用时才会执行，没有调用就会停止在yield
        baozi = yield #在它就收到内容的时候后就把内容传给baozi
        print('包子[%s]来了,被[%s]吃了'%(baozi, name))

def producer(name):
    c1 = customer('A') #它只是把c1变成一个生成器
    c2 = customer('B')
    c1.__next__()
    c2.__next__()
    for i in range(1,10,2):
        time.sleep(1)
        print('%s做了2个包子:分别是包子%s和包子%s'%(name, i, i+1))
        c1.send(i) #这一步其实就是调用next方法的同时传一个参数i给field接收，然后baozi=i
        c2.send(i+1)
        #其实这里是这样的，在send的时候只是继续执行yield下面的语句，然后去去yield，再次停在这儿

if __name__ == "__main__":
    producer('liu')
