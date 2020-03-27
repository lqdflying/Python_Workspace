# -*- coding: utf-8 -*-
'''
Created on 2017年7月7日

@author: anddy.liu
'''
salary = int(input("请输入您的工资："))

i = 1
product = []
while i <= 5:
    thing = input("请输入产品名称：")
    price = int(input("请输入产品价格："))
    product.append([thing,price])
    i = i+1
    
print("当前产品清单如下:")

for h in product:
    print(h[0])  #注意这种写法，h实际上就是Product数组第一层的值，每个h就是一个二值数组，因此h[0]就是Product的每个子数组的第一个值


m = 1
shopped = []
salaryleft = salary
while m <= 5 :
    ShopThing = input("请输入你需要购买的商品的名字,结束购物请输入n")
    if(ShopThing == "n"):
        break
    shopsum = len(product) #返回列表长度的函数
    f = 0
    while f < shopsum :
        if product[f][0] == ShopThing:
            break
        else:
            f = f+1
    if f == shopsum :
        print("没有你要的商品")
        continue
    if product[f][1] <= salary:
        print("您可以购买此商品")
        shopped.append(ShopThing)
        salaryleft = salary - product[f][1]
    else:
        print("您不能购买此商品，资金不够！")
    wanna = input("继续购物请按任意键，退出请输入n")
    if(wanna == "n"):
        break
    else:
        m = m+1
    
    
print("您当前选择商品如下：",shopped)

pay = input("是否付款或取消？输入Y付款，输入N取消：")

if pay.lower() == "y":
    print("开始付款")
elif pay.lower() == "n":
    print("结束退出")
    exit
else:
    print("错误的交互")

