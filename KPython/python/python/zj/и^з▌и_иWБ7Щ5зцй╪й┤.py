#!/usr/bin/python
#coding=utf-8
num=100
def test1():
    global num
    print(num)
    num+=2
    print(num)

def test2():
    print(num)

test1()
test2()
