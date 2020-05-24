# -*- coding:utf-8 -*-
###
# File: yield_and_from.py
# Created Date: 2020-05-24
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday May 24th 2020 10:09:28 pm
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
            return f'\tcoroutine_example()函数整个结束后的返回值[\n\t\t\t{x}\n\t\t]'
        print('send值:', x)

def coroutine_from(father):
    result = yield from coroutine_example(father)
    return f"coroutine_from()的返回值[\n\t{result}\n\t]"

coro = coroutine_from('liu')
coro.__next__()
try:
    coro.send(None)
except StopIteration as e:
    print('try-except返回值[\n\t{}\n]'.format(e.value))