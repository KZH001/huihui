#!/usr/bin/python
#coding=utf-8

from socket import *
from select import *
from time import ctime

HOST = '192.168.0.164'
PORT = 9999
BUFSIZE = 1024
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_STREAM,0)
sockfd.bind(ADDR)
sockfd.listen(5)

inputs = [sockfd]

while True:
    rs,ws,es = select(input,[],[])
    for r in rs:
        if r is rs:
            connfd,addr = sockfd.accept()
            print("connected from :",addr)
            inputs.append(connfd)
        else:
            try:
                data = r.recv(BUFSIZE).decode()
                disconnect = not data
            except socket.error:
                disconnect = True
            if disconnect:
                print (r.getpeername(),'disconnected')
                inputs.remove(t)
                r.close()
            else:
                r.send(('[%s] :%s'%(ctime(),data)),encode())

sockfd.close()
