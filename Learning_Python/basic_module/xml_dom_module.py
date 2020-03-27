# -*- coding: utf-8 -*-
'''
Created on 2018年3月11日

@author: anddy.liu
'''
import xml.dom.minidom as xmldom #用个别名
doc = xmldom.parse('movie.xml') #打开一个xml文档
xmlobject=doc.documentElement
print("标签属性".center(30,"+"))
print("nodeName:", xmlobject.nodeName)        #每一个结点都有它的nodeName，nodeValue，nodeType属性
print("nodeValue:", xmlobject.nodeValue)      #nodeValue是结点的值，只对文本结点有效
print("nodeType:", xmlobject.nodeType)
print("ELEMENT_NODE:", xmlobject.ELEMENT_NODE)
print("返回子节点列表:\n", xmlobject.childNodes)
print("获得二级子标签/节点的相关的值".center(30,"+"))
subobject_movie=xmlobject.getElementsByTagName('movie')
print("所有的tag是movie的二级子标签都会被获取并组合成一个地址列表：\n，",subobject_movie)
print("tag是movie的第一个二级子标签段的nodeName：\n",subobject_movie[0].nodeName) #大小写敏感
print("tag是movie的第一个二级子标签段的nodeValue：\n",subobject_movie[0].nodeValue) #大小写敏感
print("tag是movie的第一个二级子标签的的属性名字为title的值：\n ",subobject_movie[0].getAttribute('title'))
print("tag是movie的第一个二级子标签的的属性名字为dream的值：\n ",subobject_movie[0].getAttribute('dream'))
print("获得二级子标签/节点的之间的数据".center(30,"+"))
print("返回二级子节点列表:\n", subobject_movie[0].childNodes)
subobject_movie_type=subobject_movie[0].getElementsByTagName('type')
print("返回二级子节点列表中属性名为type的第一个数据:\n", subobject_movie_type[0].childNodes[0].data)
subobject_movie_format=subobject_movie[0].getElementsByTagName('format')
print("返回二级子节点列表中属性名为type的第一个数据：\n", subobject_movie_format[0].childNodes[0].nodeValue)
print("返回二级子节点列表中属性名为type的第二个数据：\n", subobject_movie_format[1].childNodes[0].nodeValue)
print("循环输出xml的数据".center(30,"+"))
for movie in subobject_movie:
    print("".center(20,"="))
    print("".center(20,"-")) 
    print(movie.nodeName)
    print(movie.toxml())
    movietype=movie.getElementsByTagName('type')[0]
    print(movietype.childNodes)
    print(movietype.nodeName + ":" +movietype.childNodes[0].nodeValue)
    print("".center(20,"-"))
    movieformat=movie.getElementsByTagName('format')[0]
    print(movieformat.childNodes)
    print(movieformat.nodeName + ":" +movieformat.childNodes[0].nodeValue)
    print("all element output".center(40,"-")) 
    for n in movie.childNodes:
        print(n)
    print("".center(40,"-"))
