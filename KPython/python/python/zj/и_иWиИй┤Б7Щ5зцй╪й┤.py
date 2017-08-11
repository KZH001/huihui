#!/usr/bin/python
#coding=utf-8
import time
def test1():
    num=100
    print(num)

def test2():
    num=200
    print(num)
#调用时间
    time.sleep(1)

    num=num+100
    print(num)

test2()
