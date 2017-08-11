#!/usr/bin/python
#coding=utf-8
def fun(x):
    return x **2

l = [1,2,3,4,5]
print map(fun,l)
def funm(x):
    return x ** 2
def funf(x):
    return  x >2 and x > 5
def funr(x,y):
    return x + y
l = [1,2,3,4,5]
print map(fun,l)
print filter(funf,l)
print reduce(funr,l)
