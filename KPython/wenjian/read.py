# coding=utf-8

# import sys

with open('file','r+') as f:
    s = f.read(50)
    s1 = f.readline(10)
    s2 = f.readline(10)
    s3 = f.readlines()

print s
print s1
print s2
print s3


# s = sys.stdin.readline()
# print s
