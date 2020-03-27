# -*- coding: utf-8 -*-
'''
Created on 2017年8月1日

@author: anddy.liu
'''
import random
print("Return the next random floating point number in the range [0.0, 1.0)\n",random.random()) 
print("Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)\n",random.randint(1,100))
print("Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.\n",random.choice([1,2,3,4]))
#choice就是传入一个序列，序列可以是字典，列表，元组，集合等
print("Return a 3 length list of unique elements chosen from the population sequence or set. \n",random.sample("liuquandong",3))
print("Return a random floating point number N such that a <= N <= b\n",random.uniform(1,3)) #只是在random.random的基础上新增个范围而已
y = [1,2,3,4]
random.shuffle(y)
print("Shuffle the sequence x in place.\n",y)#把一个list乱序处理