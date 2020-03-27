# -*- coding: utf-8 -*-
'''
Created on 2017年7月8日

@author: anddy.liu
'''
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
exit_flag = False
while not exit_flag:
#while True:
    for i in menu:
        print(i)
    choice = input("enter you choice,[0]for the Up layer,True for exit:")
    if choice == "True":
        exit_flag = True
    elif choice == "0":
        break
    elif choice in menu:
        while not exit_flag:
            for n in menu[choice]:
                print("\t",n)
            choice2 = input("enter you choice,[0]for the Up layer,True for exit:")
            if choice2 == "True":
                exit_flag = True
            elif choice2 == "0":
                break
            elif choice2 in menu[choice]:
                while not exit_flag:
                    for m in menu[choice][choice2]:
                        print(m)
                    choice3 = input("enter you choice,[0]for the Up layer,True for exit:")
                    if choice3 == "True":
                        exit_flag = True
                    elif choice3 == "0":
                        break
                    elif choice3 in menu[choice][choice2]:
                        while not exit_flag:
                            for g in menu[choice][choice2][choice3]:
                                print(g)
                            choice4 = input("enter you choice,[0]for the Up layer,True for exit:")
                            if choice4 == "True":
                                exit_flag = True
                            elif choice4 == "0":
                                break

#break是结束当前循环，而exit则是退出整个代码
