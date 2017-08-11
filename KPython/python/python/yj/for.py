#!/usr/bin/python
#coding=utf-8
for i in [1,2,3,4,5] :
    print i,
print ""
for i in (1,2,3,4,5) :
    print i,
print ""
for i in {1,2,3,4,5} :
    print i,
print ""
for i in "hello world" :
    print i,
print ""
for i in {'a':1,'b':2} :
    print i,
print ""
sum = 0
for i in range(1,101):
    sum += i
print sum
