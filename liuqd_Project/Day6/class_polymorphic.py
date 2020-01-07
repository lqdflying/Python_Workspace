# -*- coding: utf-8 -*-
'''
Created on 2017年9月1日

@author: anddy.liu
'''
#多态——一个接口，多种实现
class Animal(object):
    def __init__(self, name): # Constructor of the class
        self.name = name
    def talk(self): # Abstract method, defined by convention only
        pass #raise NotImplementedError("Subclass must implement abstract method")
    @staticmethod  #这个装饰器用来实现多态，记住
    def func(obj): #一个接口，多种形态
        obj.talk()

    
class Cat(Animal):
    def talk(self):
        print('%s: 喵喵喵!' %self.name)


class Dog(Animal):
    def talk(self):
        print('%s: 汪！汪！汪！' %self.name)




c1 = Cat('小晴')
d1 = Dog('李磊')

Animal.func(c1)
Animal.func(d1)