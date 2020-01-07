# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import xml.etree.ElementTree as et  
tree = et.parse("liuqd.xml")
root = tree.getroot()
print(root)
print(root.tag)
print("遍历xml文档".center(50,"+"))
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text,i.attrib) #tag取标记，text取内容，attrib取属性

print("遍历year节点".center(50,"+"))
for node in root.iter("year"):
    print(node.tag,node.text)


