# -*- coding:utf-8 -*-
###
# File: killers_ring.py
# Created Date: 2020-08-11
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday August 12th 2020 11:17:54 am
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import queue
people = list(range(1,42))

#版本一
'''
def update_data(var):
    tmp = []
    for i in range(1,len(var)+1):
        if i%3:
            tmp.append(var[i-1])
    return tmp

result = people
i = 1
while len(result) > 2:
    length = len(result)%3
    if length:
        end = result[-(length):]
        result = update_data(result)
        print(result)
        result = end + result[:-(length)]
        print("第%s次:\n"%i,result)
    else:
        result = update_data(result)
        print("第%s次:\n"%i,result)
    i += 1
'''

#版本二
q = queue.Queue()
for i in people:
    q.put(i)

while q.qsize() > 2:
    var1 = q.get()
    var2 = q.get()
    var3 = q.get()
    q.put(var1)
    q.put(var2)

while not q.empty():
    print(q.get())