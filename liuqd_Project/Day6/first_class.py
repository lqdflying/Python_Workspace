# -*- coding: utf-8 -*-
'''
Created on 2017年8月7日

@author: anddy.liu
'''
#类的定义
class Role(object): 
    n = 123 #这个是个类变量
    name = "default_name"
    n_list = []
    def __init__(self,name,role,weapon,life_value=100,money=15000):
        #这其实是一个构造函数，作用是在实例化时做一些类的初始化的工作，比如内存开辟等
        self.name = name #实例变量，就是赋给实例的变量，也称之为静态属性，实例变量的作用域就是实力本身，不同的实例之间无法共享
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money

    def shot(self): #类的方法1
        print("shooting...")
    
    def got_shot(self): #类的方法2，方法就是功能
        print("ah...,I got shot...")
    
    def buy_gun(self,gun_name): #类的犯法3，这里还传入了一个变量，这个变量被称之为动态变量
        print("%s just bought %s" %(self.name,gun_name))

print(Role) #就算是下边不调用，在内存里也是存在的，这里print能出结果就是证明、
print("类变量可以不经过实例化就直接打印：",Role.n)
#类的实例化

r1 = Role("Alex","police","AK47") #生成一个角色，一个类初始化后，需要赋予一个变量，这样才好多次使用，其实是保存一个入口
r2 = Role("Jack","terrorist","B22") #生成一个角色\
#r1和r2又叫做Role这个类的实例
#类的执行
r1.buy_gun("ak47")

r1.name = "changename" #利用这个修改属性内容
r1.new = "new_variable" #实例化以后，这个实例的属性是可以继续利用这个方法增加的
del r1.money #实例化后，这个实例的属性还可以随意删除
r1.buy_gun("ak47")
print(r1.new)
#print(r1.money) #这句会报错，因为已经被del了

r1.n = "change n" #这里实际上是为r1做了n这个变量的实例化，那么对于r1来说，这个n就不是类变量了，而是直接物化存在于r1的内存里的普通实例变量
print(r2.n) #会发现r1修改了类变量以后，r2里的类变量不受影响

r1.n_list.append("var1") #这里实际上做的不是r1的list的实例化，而是为类变量赋值，那么这个赋值就会传递到r2中去
Role.n_list.append("var2") #这样对类变量赋值也是可以的
print(r2.n_list)

r1.n_list = ["myvar"] #这样就不是通过r1位类变量赋值了，而是把r1又物化了一个n_list的list,这个list会覆盖掉类变量list
print(r1.n_list,r2.n_list)





