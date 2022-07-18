# -*- coding: utf-8 -*-
# 客户端
import socket


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('127.0.0.1', 8000))
while True:
    print('client here')
    data = input('reply >>')
    clientsocket.send(data.encode())
    if not data:
        break
    newdata = clientsocket.recv(1024)
    print('Received: ', repr(newdata.decode()))
clientsocket.close()
