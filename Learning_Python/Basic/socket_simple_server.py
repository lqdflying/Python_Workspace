# -*- coding:utf-8 -*-
###
# File: socket_simple_server.py
# Created Date: 2020-05-03
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday May 3rd 2020 7:25:20 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import socket

server = socket.socket() #获得socket实例

server.bind(("localhost",10999)) #绑定ip port
server.listen()  #开始监听
while True:
    print("等待客户端的连接...")
    conn,addr = server.accept() #接受并建立与客户端的连接,程序在此处开始阻塞,只到有客户端连接进来...
    print("新连接:",addr )
    while True:
        data = conn.recv(1024)
        if not data:
            print("客户端断开了...")
            break
        print("收到消息:",data.decode("utf-8"))
        msg = "服务器返回消息: %s"%data.decode("utf-8")
        conn.send(msg.encode("utf-8")) #服务器端发送消息
server.close()