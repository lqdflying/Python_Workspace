# -*- coding:utf-8 -*-
###
# File: killers_ring.py
# Created Date: 2020-08-11
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Thursday August 13th 2020 8:43:52 am
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

print("版本一(17lines):")

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
    result = update_data(result)
    result = result[(len(result)-length):] + result[:(len(result)-length)]
    print("第%s次处理后:\n"%i,result)
    i += 1


print("版本二(13lines):")
q = queue.Queue()
for i in people:
    q.put(i)

while q.qsize() > 2:
    var1 = q.get()
    var2 = q.get()
    var3 = q.get()
    q.put(var1)
    q.put(var2)

print(list(q.queue))
