# -*- coding:utf-8 -*-
###
# File: socket_socketclient.py
# Created Date: 2020-05-09
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 9th 2020 11:03:40 am
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import socket

HOST, PORT = "localhost", 9990
# sock.connect((HOST, PORT))
def main():
    while True:
        print("建立服务器端的连接")
        sock = socket.socket()
        sock.connect((HOST, PORT))
        while True:
            data = input('Input [a-z]:>>')
            if data == "bye":
                print("按要求退出!")
                sock.close()
                exit()
            sock.sendall(bytes(data + "\n", "utf-8"))
            received = str(sock.recv(1024), "utf-8")
            if not received: 
                sock.close()
                break
            print("Sent:     {}".format(data))
            print("Received: {}".format(received))

if __name__ == "__main__":
    main()