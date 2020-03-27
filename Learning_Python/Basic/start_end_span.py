# -*- coding: utf-8 -*-
'''
Created on 2017年8月11日

@author: anddy.liu
'''
names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei",32]
names2 = "liuqd"
print(names[::-1])
print(names2[::-1])
# l[start:end:span]
# 遍历 [start,end)，间隔为 span，当 span>0 时顺序遍历, 当 span<0 时，逆着遍历。
# start 不输入则默认为 0，end 不输入默认为长度。