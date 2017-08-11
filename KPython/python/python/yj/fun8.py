#!/usr/bin/pyrthon
#coding=utf-8
#递归recursive
def recursive(n):
    if n <= 1:
        return 1
    return(n * recursive(n - 1))
r = recursive(5)
print('5! = %d'%r)
print "...."
def recursive(n):
    if n > 5:
        return 1
    return(n * recursive(n + 1))
k = recursive(6)
print('6!= %d'%k)
