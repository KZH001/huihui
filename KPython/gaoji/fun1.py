#coding=utf-8
import datetime
#装饰器 函数装饰类
#类装饰器
class Begin(object):
    def __init__(self,obj):
        self.func = obj
        #自动化调用
    def __call__(self,*args,**kwarg):
        print "时间"
        self.func(*args,**kwarg)

# 装饰器
@Begin
#取得时间
def getTime(a,b,c,d):
    print a,b,c,d
    print datetime.datetime.now()
#一
# begin(getTime)()
#二
getTime(6,7,8,9)
