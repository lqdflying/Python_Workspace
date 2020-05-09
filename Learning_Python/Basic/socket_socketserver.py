# -*- coding:utf-8 -*-
###
# File: socket_socketserver.py
# Created Date: 2020-05-09
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 9th 2020 3:33:02 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import socketserver
# class myserver(socketserver.BaseRequestHandler):
class myserver(socketserver.StreamRequestHandler): #继承StreamRequestHandler后类写法会变
    def handle(self):
        try:
            print("新客户端连入--Ip:{0} Port:{1}".format(self.client_address[0], self.client_address[1]))
            while True:
                # self.data = self.request.recv(1024).strip()
                self.data = self.rfile.readline().strip() #继承StreamRequestHandler后要用rfile
                if not self.data:
                    self.request.sendall("输入不能为空".encode('utf8'))
                    continue
                print(self.data.decode('utf8'))
            # just send back the same data, but upper-cased
                # self.request.sendall(self.data.upper())
                self.wfile.write(self.data.upper()) #继承StreamRequestHandler后要用wfile
        except BrokenPipeError:
            print("客户端断开连接")

    def finish(self):
        print("此处可以进行收尾的操作,比如关闭文件等")

def main():
    HOST, PORT = "localhost", 9990
    server = socketserver.ThreadingTCPServer((HOST, PORT), myserver)    #实例化一个多线程TCPServer
    print('Wait client . . .') 
    server.serve_forever()

if __name__ == "__main__":
    main()
