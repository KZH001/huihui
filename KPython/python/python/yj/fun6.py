#!/usr/bin/python
#coding=utf-8
#zx
def fun(a,b=10,*c):
    print a
    print b
    print c
fun(1,2,3,4,5)
print "........."
def kk(a,b=10,*c,**d):
    print a
    print b
    print c
    print d
kk(1,2,3,4,c=5,d=6)

# # 3x
#
# def ll(a,b=10,*c,d):
#     print (a)
#     print (b)
#     print (c)
#     print (d)
#
# ll(1,2,3,4,d=5)
