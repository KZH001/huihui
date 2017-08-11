#!/usr/bin/python
#coding=utf-8
#地址传参
def fun(i,j):
    print i,j
fun(1,2)
print "....."
# 关键字传参
def fun(l,k):
    print l,k
fun(l=3,k=4)
print "......."
# *传参
def fun(w,o):
    print w,o
j=[2,3]
fun(*j)
print "......."
# **传参
def kk(a,b):
    print a,b

c={'a':2,'b':1}
kk(**c)
