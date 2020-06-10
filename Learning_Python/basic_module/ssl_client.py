# -*- coding:utf-8 -*-
###
# File: ssl_client.py
# Created Date: 2020-06-10
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday June 10th 2020 3:08:22 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import ssl,pprint,socket
context = ssl.create_default_context()
conn = context.wrap_socket(socket.socket(socket.AF_INET),server_hostname="www.python.org")
conn.connect(("www.python.org", 443))
print("输出获取到的服务器端证书:".center(30,"+"))
pprint.pprint(conn.getpeercert())
conn.sendall(b"HEAD / HTTP/1.0\r\nHost: linuxfr.org\r\n\r\n")
pprint.pprint(conn.recv(1024).split(b"\r\n"))