#!/usr/bin/python
#coding=utf-8
#位置
def fun(a,b):
    print a,b
fun(1,2)
#参数默认值
def k(a,b=12):
    print a,b
k(1)
#收集参数
def kk(*a):
    print a
kk(1,2,3)
# 收集字典函数
def kkk(**b):
    print b
kkk(a=1,b=2,c=3)
