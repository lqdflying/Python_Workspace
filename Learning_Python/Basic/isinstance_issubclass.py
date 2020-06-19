# -*- coding:utf-8 -*-
###
# File: isinstance_issubclass.py
# Created Date: 2020-06-19
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday June 19th 2020 10:21:19 pm
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


print("object".center(20,"+"))
print("Vehicles():--->",Vehicles())
print("Car():--->",Car())
print("a:--->",a)
print("b:--->",b)

print("type".center(20,"+"))
print(f"type(Car()):--> {type(Car())}   and is its type 'Car'?----> {type(Car()) == Car} ",)
print(f"type(Vehicles()):--> {type(Vehicles())}   and is its type 'Vehicles'?----> {type(Vehicles()) == Vehicles} ",)
print(f"type(a):--> {type(a)}   and is its type 'Car'?----> {type(a) == Car} ",)
print(f"type(b):--> {type(b)}   and is its type 'Vehicles'?----> {type(b) == Vehicles} ",)

print("isinstance".center(20,"+"))
print(f"isinstance(a, object): {isinstance(a, object)}")
print(f"isinstance(a, Car): {isinstance(a, Car)}")
print(f"isinstance(a, Vehicles): {isinstance(a, Vehicles)}")
print(f"isinstance(a, (Car,Vehicles)): {isinstance(a, (Car,Vehicles))}")
print(f"isinstance(a, str): {isinstance(a, str)}")
print(f"isinstance(a, (Car,str)): {isinstance(a, (Car,str))}")

print("issubclass".center(20,"+"))
print("issubclass(Car, object):--->", issubclass(Car, object)) 
print("issubclass(Car, Vehicles):--->", issubclass(Car, Vehicles)) 
print("issubclass(Car, list):--->",issubclass(Car, list)) 
print("issubclass(Car, Car):--->",issubclass(Car, Car)) 
print("issubclass(Car, (list, Vehicles)):--->",issubclass(Car, (list, Vehicles)))