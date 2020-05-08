# -*- coding:utf-8 -*-
###
# File: socket_socketserver.py
# Created Date: 2020-05-09
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 9th 2020 12:52:55 am
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
        while True:
            self.data = self.request.recv(1024).strip()
            if not self.data:
                print("The client disconnects actively!")
                break
            print("Ip:{0} Port{1}:".format(self.client_address[0], self.client_address[1]))
            print(self.data.decode('utf8'))
        # just send back the same data, but upper-cased
            self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9990
    server = socketserver.ThreadingTCPServer((HOST, PORT), myserver)    #实例化一个多线程TCPServer
    print('Wait client . . .') 
    server.serve_forever()