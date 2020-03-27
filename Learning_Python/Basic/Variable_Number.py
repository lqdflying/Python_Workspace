# -*- coding: utf-8 -*-
'''
Created on 2017年8月7日

@author: anddy.liu
'''
anInt = 1
along = -555555555555
afloat = 3.141595468565
acomplex = 1.334+4.5433j
print("各种类型的数据".center(50,"+"))
print("整型：",type(anInt),anInt)
print("长整型也是整型：",type(along),along)
print("浮点型：",type(afloat),afloat)
print("复数：",type(acomplex),acomplex)
print("各种类型的数据进行转换".center(50,"+"))
print("整型转浮点型：",float(anInt))
print("长整型转浮点型：",float(along))
print("长整型转复数：",complex(along))
print("浮点型转整型：",int(afloat))
#print("复数转浮点型：",type(acomplex),float(acomplex)) #提示：can't convert complex to float
#print("复数转整型：",type(acomplex),int(acomplex)) #提示：can't convert complex to int