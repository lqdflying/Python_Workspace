# -*- coding: utf-8 -*-
'''
Created on 2017年8月2日

@author: anddy.liu
'''
#这就是一个验证码函数，while判断的作用是，如果生成的验证码都是数字，就重新生成一次
import random
checkcode = ""
while checkcode.isdigit() == True or checkcode == "":
    checkcode = ""
    for i in range(5):
        current = random.randint(0,4)
        if current == i:
            tmp = chr(random.randint(65,90)) 
        else:
            tmp = random.randint(0,9)
        checkcode+=str(tmp)
print(checkcode)