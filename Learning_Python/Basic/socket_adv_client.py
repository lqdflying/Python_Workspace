# -*- coding:utf-8 -*-
###
# File: socket_adv_client.py
# Created Date: 2020-05-03
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday May 6th 2020 10:58:33 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import socket,sys,os,struct

currentdir = os.path.dirname(__file__)
client = socket.socket()

client.connect(("localhost",10111))

'''
def recvall(sock, n):
    # Helper function to recv n bytes or return None if EOF is hit
    data = bytearray() #初始len(data)=0,因为为空
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data.extend(packet)
    return data
'''

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send( msg.encode("utf-8") )
    
    res_size_raw  = client.recv(4) #接收这条命令执行结果的大小
    res_size = struct.unpack('I', res_size_raw)[0]
    total_rece_size = int(res_size)
    print("total size:",res_size)
    #client.send("准备好接收了,发吧loser".encode("utf-8")) #encode是讲str处理成bytes
    received_size = 0 #已接收到的数据
    cmd_res = b''
    with open("%s/test_copy.log"%currentdir,"wb") as f:#把接收到的结果存下来,一会看看收到的数据 对不对
        while received_size != total_rece_size: #代表还没收完
            data = client.recv(1024)
            received_size += len(data) #为什么不是直接1024,还判断len干嘛,注意,实际收到的data有可能比1024少
            cmd_res += data
            # print("接收到一次数据:",cmd_res)
            # print(received_size)
        else:
            print("数据收完了",received_size)
            #print(cmd_res.decode())
            f.write(cmd_res) #把接收到的结果存下来,一会看看收到的数据 对不对
        print("结果".center(20,"+")) #命令执行结果
        print(cmd_res.decode())
client.close()