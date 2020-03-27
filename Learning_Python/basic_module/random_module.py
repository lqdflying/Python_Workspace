# -*- coding: utf-8 -*-
'''
Created on 2018年3月3日

@author: anddy.liu
'''
import random
x=['1','2','a','b','c','d','liu','gogo'] #这是一个list
print("random()的返回时：0-1之间的任意数：\n",random.random())
print("getrandbits函数实在bit级别上进行控制，以\"二进制\"的风格控制每个bit上的随机量：\n",random.getrandbits(3))
print("choice是从指定的list中返回随机的元素：\n",random.choice(x))
print("sample是从指定的list中返回随机执行的几个元素：\n",random.sample(x,2)) #这里是指定了两个元素
random.shuffle(x)
print("shuffle是将指定的list重新排序: \n",x)
print("randrange从给定的范围返回随机项。可以仅仅指定结束的stop： \n",random.randrange(2));
print("randrange从给定的范围返回随机项。可以start，stop，step都指定： \n",random.randrange(1,10,2));
print("生成一个指定范围的整数: \n",random.randint(1,10))
