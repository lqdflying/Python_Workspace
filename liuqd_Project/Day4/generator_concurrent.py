# -*- coding: utf-8 -*-
'''
Created on 2017年7月16日

@author: anddy.liu
'''
import time

def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
        baozi = yield
        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))

def producer():
    c = consumer("liuqd") #定义生成器1，【注】：仅仅是具体的定义
    c2 = consumer("lium") #定义生成器2，【注】：仅仅是具体的定义
    print("c",c)
    print("c2",c2)
    c.__next__()#需要先制执行一次，为的是首先print("%s 准备吃包子啦!" %name)，之后让代码在第一次while循环的时候就在baozi这里中断并跳出
    c2.__next__()#需要先制执行一次，为的是首先print("%s 准备吃包子啦!" %name)，之后让代码在第一次while循环的时候就在baozi这里中断并跳出
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i) 
#c.__next__()跳出后就跑到这里了，给baozi回传一个值，这时候当c再次执行next的时候，下边的print("包子[%s]来了,被[%s]吃了!" %(baozi,name))就有值可以显示了
        c2.send(i)
#c2.__next__()跳出后就跑到这里了，给baozi回传一个值，这时候当c再次执行next的时候，下边的print("包子[%s]来了,被[%s]吃了!" %(baozi,name))就有值可以显示了

producer()