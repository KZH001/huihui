#!/usr/bin/python
#coding=utf-8
#协程 lock
# from time import sleep
# from greenlet import greenlet
#
# def test1():
#     while True:
#         sleep(1)
#         print 2
#         gr2.switch()
#         print 4
#
# def test2():
#     while True:
#         sleep(1)
#         print 1
#         gr1.switch()
#         print 3
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
#
# gr1.switch()
# gr2.switch()

from time import sleep
from greenlet import greenlet

def test1():
    sleep(1)
    print 2
    gr2.switch()
    print 4

def test2():
    sleep(1)
    print 1
    gr1.switch()
    print 3

gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()
gr2.switch()
