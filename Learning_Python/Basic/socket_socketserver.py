# -*- coding:utf-8 -*-
###
# File: socket_socketserver.py
# Created Date: 2020-05-09
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 9th 2020 10:19:14 am
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import socketserver
class myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print("新客户端连入--Ip:{0} Port:{1}".format(self.client_address[0], self.client_address[1]))
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                self.request.sendall("输入不能为空".encode('utf8'))
                continue
            print(self.data.decode('utf8'))
        # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())
    def finish(self):
        print("客户端连接断开")

if __name__ == "__main__":
    HOST, PORT = "localhost", 9990
    server = socketserver.ThreadingTCPServer((HOST, PORT), myserver)    #实例化一个多线程TCPServer
    print('Wait client . . .') 
    server.serve_forever()
