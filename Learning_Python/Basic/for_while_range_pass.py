# -*- coding: utf-8 -*-
'''
Created on 2017年8月17日

@author: anddy.liu
'''
'''
count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")
    
    

for i in range(0,5,1):
    var = input("你还想继续吗，输入y或n")
    if var == "y" :
        print("那你继续")
    elif var == "n":
        print("那就不要继续了")
        break
    else:
        print("错误的输入")
        print("第",i+1,"次循环输入错误")    
    i+=1


names = ["LiuQuandong","LiuMing",["name1","name2"],"WuHongwei"]
for i in range(names.__len__()):
    print(i,names[i])

'''
while True:
    pass
















