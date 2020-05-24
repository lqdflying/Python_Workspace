# -*- coding: utf-8 -*-
'''
Created on 2017年8月17日

@author: anddy.liu
'''

count = 0
while count < 5:
    print (count, " 小于 5")
    count = count + 1
else:
    print (count, " 大于或等于 5")
    
    

for i in range(0,5,1):
    var = input("你还想继续吗，输入y或n:")
    if var == "y" :
        print("那你继续")
    elif var == "n":
        print("那就不要继续了")
        break
    else:
        print("错误的输入")
        print("第",i+1,"次循环输入错误")    
    i += 1


names = ["LiuQuandong","LiuMing",["name1","name2"],"WuHongwei"]
for i in range(names.__len__()):
    print(i,names[i])

print("测试continue,break和return".center(30,"+"))

def while_test(name):
    i = 1
    while i < 3:
        if name == "liu":
            print('继续循环')
            # continue
        elif name == "quan":
            i += 1
            continue
        elif name == "dong":
            break
        else:
            return f"{name}:while_test函数整个都会停止,连函数体while之外的下边的代码都不会执行"
        i += 1
    print(f"{name}:仅仅退出while循环而不是退出函数体的话,这句是会执行的")
print(while_test('liu'))
print(while_test('quan'))
print(while_test('dong'))
print(while_test('other'))

