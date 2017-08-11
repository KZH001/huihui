#!/usr/bin/python
#coding=utf-8
#类的继承
class kk(object):
    name="kang"
    def aa(self):
        print "千万资产"
class zz(kk):
    pass

bb = zz()
print bb.name
bb.aa()
#多继承

class kk(object):
    name="kang"
    age=100
class zz(object):
    name="zeng"
    sex='man'
class hh(kk,zz):
    pass
A=hh()
print A.age
print A.sex
print A.name

class kk(object):
     #不被继承
    def __init__(self):
        self.job="kang"
        self.__name='zeng'

    def name(self,n):
        #权限
        if n == 1:
            return self.__name
        else:
            return "sorry"

class zz(kk):
    pass

q=kk()
print q.job
print q.name(1)
