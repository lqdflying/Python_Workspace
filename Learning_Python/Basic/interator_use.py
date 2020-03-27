# -*- coding: utf-8 -*-
'''
Created on 2017年10月31日

@author: anddy.liu
'''
#import sys
newlist = [1,2,3,4]
it1 = iter(newlist)    # 创建迭代器对象
for x in it1:
    print (x, end="|")   #end:string appended after the last value, default a newline.
print("\n")
it2 = iter(newlist) 
while True:
    try:
        print(next(it2))
    except StopIteration:
        #sys.exit()
        print("ggogogogo")
        break
        #print("ggogogogo")

print("\n")
it3 = iter(newlist)
while True:
    try:
        print(it3.__next__())
    except StopIteration:
        #sys.exit()
        print("aaaaaaa")
        break
        #print("ggogogogo")
