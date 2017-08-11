#!/usr/bin/python
#coding=utf-8
#super
class Kk(object):
    def __init__(self):
        self.height=170
    def about(self,name):
        print "{} is about {}".format(name,self.height)
class Girl(Kk):
    def __init__(self):
        self.weight=100
        #子用父
        super(Girl,self).__init__()

    def about(self,name):
        print "{} is a girl,she is about {}and her weight is {}".format(name,self.height,self.weight)

        super(Girl,self).about(name)

kang=Girl()
kang.about("zenghui")

super(Girl,kang).about("fenghuang")
