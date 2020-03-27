# -*- coding: utf-8 -*-
'''
Created on 2017年7月7日

@author: anddy.liu
'''
'''

names = ["LiuQuandong","LiuMing",["name1","name2"],"WuHongwei"]


print(names[0::3]) #从开始打印到结束。步长是3，结果是可以打印两个数值
print(names[0:-1:3]) #从开始打印到结束。步长是3，结果是可以打印一个数值→ 因为顾头不顾尾

for i in names[2]:
    print(i)
print("\n")
'''

product = [['usr1', 3000], ['usr2', 4000], ['usr4', 300], ['china1', 500], ['uar90', 90]]
print("第一种打印子数组第一列的方法：")
for m in product:
    print(m[0])
    
print("第二种打印子数组第一列的方法：")    
for m,n in product:
    print(m)
    
print(product.index(['usr2', 4000]))  #打印数组下标,也就是索引index编号




