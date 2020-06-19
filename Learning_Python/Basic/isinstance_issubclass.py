# -*- coding:utf-8 -*-
###
# File: isinstance_issubclass.py
# Created Date: 2020-06-19
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday June 19th 2020 5:06:45 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
# Python program to demonstrate 
# issubclass() 


# Defining Parent class 
class Vehicles: 

	# Constructor 
	def __init__(self,vehicleType='default'): 
		print('Vehicles is a', vehicleType) 

# Defining Child class 
class Car(Vehicles): 

	# Constructor 
	def __init__(self): 
		super().__init__('Car') 
a = Car()
b = Vehicles('boat')

print(f"type(Vehicles()):{type(Vehicles())},and is its type Vehicles? {type(Vehicles()) == Vehicles} ",)
print("Vehicles():--->",Vehicles())
print(f"type(Car()):{type(Car())},and is its type Car? {type(Car()) == Car} ",)
print("Car():--->",Car())
print("type(a):--->",type(a))
print("a:--->",a)
print("type(b):--->",type(b))
print("b:--->",b)

# Driver's code
print("issubclass(Car, Vehicles):--->", issubclass(Car, Vehicles)) 
print("issubclass(Car, list):--->",issubclass(Car, list)) 
print("issubclass(Car, Car):--->",issubclass(Car, Car)) 
print("issubclass(Car, (list, Vehicles)):--->",issubclass(Car, (list, Vehicles)))