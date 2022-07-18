# -*- coding: utf-8 -*-
# 服务器
# 套接字原理 https://www.cnblogs.com/yblackd/p/12910340.html
import socket


# AF_INET为IPv4网络协议套接字类型
# SOCK_STREAM指的是TCP协议（sock_dgram为UDP协议）
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8000))
serversocket.listen(1)
clientsocket, clientaddress = serversocket.accept()
print('Connection from ', clientaddress)
while True:
    print('server here')
    data = clientsocket.recv(1024)
    if not data:
        break
    print('Received from client: ', repr(data.decode()))
    newdata = input('replt >>')
    clientsocket.send(newdata.encode())
clientsocket.close()
serversocket.close()
