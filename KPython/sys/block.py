#!/usr/bin/python
#coding=utf-8

from socket import *
from time import sleep

def start():
    try:
        sock = socket(AF_INET,SOCK_STREAM)
        sock.bind(('192.168.0.164',9999))
        sock.listen(5)
    except Exception as e:
        print "fail"
        exit(0)
    while True:
        sock.setblocking(0)
        try:
            clientsock,clientaddr = sock.accept()
            buf = clientsock.recv(1024)
            clientsock.close()
        except:
            pass
        sleep(2)
        print "++++++"

if __name__ == "__main__":
    start()
