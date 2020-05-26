# -*- coding:utf-8 -*-
###
# File: coroutine_pre.py
# Created Date: 2020-05-24
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Tuesday May 26th 2020 9:23:40 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
def coroutine_example(name):
    print('start coroutine...name:', name)
    x = yield name #调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
    print('send值:', x)
    return 'coroutine_example返回的值' 
#这句会导致这个生成器coroutine_example(),给它send一次的值后(注意send的同时代码会继续从"x = yield name"这里往下执行)

def grouper2():
    result2 = yield from coroutine_example('Zarten') #在此处暂停，等待子生成器的返回后继续往下执行
    print('result2的值：', result2)
    return result2

def grouper():
    result = yield from grouper2() #在此处暂停，等待子生成器的返回后继续往下执行
    print('result的值：', result)
    return result

def main():
    g = grouper() #调用生成器
    next(g) #初始化'result = yield from grouper2()'右半部分,也就是grouper2()
    try:
        g.send(10)
    except StopIteration as e:
        print('返回值：', e.value)

if __name__ == '__main__':
    main()