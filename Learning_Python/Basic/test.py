# -*- coding:utf-8 -*-
###
# File: test.py
# Created Date: 2020-05-24
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday May 24th 2020 5:11:18 pm
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

    while True:
        x = yield name #调用next()时，产出yield右边的值后暂停；调用send()时，产出值赋给x，并往下运行
        if x is None:
            return 'zhihuID: Zarten'
        print('send值:', x)

coro = coroutine_example('Zarten')
next(coro)
print('send的返回值:', coro.send(6))
# coro.send(None)
try:
    coro.send(None)
except StopIteration as e:
    print('返回值：', e.value)