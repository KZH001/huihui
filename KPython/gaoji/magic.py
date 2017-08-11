# coding=utf-8
# 魔法方法  特殊功能  自动化运行

class Magic(object):
    '''This is Magic doc'''
    pass
print dir(Magic)
#方法

m = Magic()
print dir(m)
print "========"
print Magic.__module__
print Magic.__class__
print Magic.__doc__
