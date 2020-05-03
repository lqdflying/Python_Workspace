# -*- coding:utf-8 -*-
###
# File: socket_simple.client.py
# Created Date: 2020-05-03
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday May 3rd 2020 4:35:48 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import socket

client = socket.socket()

client.connect(("localhost",10999))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:
        continue
    client.send( msg.encode("utf-8") )
    data = client.recv(1024)
    print("来自服务器:",data.decode("utf-8"))
client.close()