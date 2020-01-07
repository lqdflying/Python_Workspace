# -*- coding: utf-8 -*-
'''
Created on 2017年7月8日

@author: anddy.liu
'''
#key尽量不要写中文
catalog = {
    "欧美":{
        "www.youporn.com": ["很多免费的,世界最大的","质量一般"],
        "www.pornhub.com": ["很多免费的,也很大","质量比yourporn高点"],
        "letmedothistoyou.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "x-art.com":["质量很高,真的很高","全部收费,屌比请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","听说是收费的"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安","服务器在国外,慢"]
    }
}

subcatalog = {
    "欧美":{
        "meizi":["1","2"]
        },
    "china":"gogo",
    "japan":"nono"
    }

catalog.setdefault(1,{1:["1","2"]})
catalog.setdefault("日韩",{"sina":["1","2"]})
#setdefault的作用是，如果字典里有key，那么不会修正，而是保持输出，如果字典里没有key那么会默认是添加一个新的key/value

catalog["大陆"]["1024"][1] = "missing" #如果key是字符串类型，那么print必须要加引号，如果key是int类型，那么print可以不加引号
#这种就是强制修改或增加了
print(catalog[1])
print(catalog)

catalog.update(subcatalog)  #使用update进行两个字典的合并
print('''两个字典做合并，取最大集合,由于是使用subcatalog去更新catalog，因此如果subcatalog里有key值
是和catalog里一致的，那么catalog会被更新，如果subcatalog里有key是catalog里没有的，那么catalog会增加：\n------>\n''',catalog)
print("-------------------")
print("字典转列表：----->\n",catalog.items())

print("\n","创建一个空列表".center(50,"+"),"\n")

c = dict.fromkeys([0,1,2,3,4,5,6,7],{"for":["myname",         #字典里边嵌套数组
                                     ["subname","subname2"],  #数组里边套子数组
                                     {"liu":"quan",           #数组里边套子字典
                                      "Liu":"dong",
                                      "MySub":
                                      [                       #子字典里边又套自数组
                                          "sub_sub_name1",
                                          "sub_sub_name2"
                                          ]
                                      }
                                     ]
                                     }
                  ) 

'''
#★ 第一个Tips：注意这个原理，[]括起来就是数组，{}套起来是字典，数组和字典都可以套子数组和子字典，并且支持各种相互嵌套，只要分清楚就行
d = dict.fromkeys(
    [0,1,2,3],
    {
        "Other":[
            "myname",
            [
                "subname",
                "subname2"
                ],
                 {
                     "mysub":
                     [
                         "Sub_sub_name1",
                         "Sub_sub_name2"
                         ]
                     }
            ]
        }
    )

print(d)
'''
print(c)

c[0]["for"][0] = "othername"

'''
第二个Tips：注意这里，如果修改了某个key的值，那么整个字典的其他key的值也就变了，这就是dict.fromkeys整个方法的妙用，有点类似指针copy
'''

print(c)


