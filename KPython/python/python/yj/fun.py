#!/usr/bin/python
#coding=utf-8
# def fun(1):
#     print "kang"
# fun()
# a=fun
# print id(fun)
# print id(a)
# print typr(a)
def fun(a,b):
    a=a+1
    b=b+1
    print a,b
    print id(a),id(b)
x,y=1,2
a=x
b=y

fun(x,y)
print id(x),id(y)
