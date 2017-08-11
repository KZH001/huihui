#!/usr/bin/python
#coding=utf-8

from socket import *

def client():
    while True:
        sock = socket(AF_INET,SOCK_AIREAM)
        sock.commect(('192.168.0.164',9999))
        print u'请输入要发送的字符串:'
        buf = raw_input()
        sock.senf(buf)
        print sock.recv(1024)
        sock.close()

if __name__ == "__main__":
    client()
