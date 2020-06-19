# -*- coding:utf-8 -*-
###
# File: isinstance_issubclass.py
# Created Date: 2020-06-19
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday June 19th 2020 6:14:49 pm
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
		# print('Vehicles is a', vehicleType) 
		self.vehicleType = vehicleType

# Defining Child class 
class Car(Vehicles): 
	# Constructor 
	def __init__(self): 
		super().__init__('Car') 
a = Car()
b = Vehicles('boat')

print("Vehicles():--->",Vehicles())
print("Car():--->",Car())
print("a:--->",a)
print("b:--->",b)

print(f"type(Car()):{type(Car())},and is its type Car? {type(Car()) == Car} ",)
print(f"type(a):{type(a)},and is its type Car? {type(a) == Car} ",)

print(f"type(Vehicles()):{type(Vehicles())},and is its type Vehicles? {type(Vehicles()) == Vehicles} ",)
print(f"type(b):{type(b)},and is its type Vehicles? {type(b) == Vehicles} ",)

# Driver's code
print("issubclass(Car, Vehicles):--->", issubclass(Car, Vehicles)) 
print("issubclass(Car, list):--->",issubclass(Car, list)) 
print("issubclass(Car, Car):--->",issubclass(Car, Car)) 
print("issubclass(Car, (list, Vehicles)):--->",issubclass(Car, (list, Vehicles)))