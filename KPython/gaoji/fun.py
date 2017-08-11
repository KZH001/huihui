# coding=utf-8
# 装饰器   对类的二次操作
# 使之更加灵活
# 函数装饰器
#函数装饰函数
#导入当下时间
# import datetime
#
# #闭包
# # 修饰函数
# def begin(func):
#     def wrapper():
#         print "现在时间:"
#         func()
#         #    返回闭包
#     return wrapper
# #
# # 装饰器
# @begin
# #取得时间
# def getTime():
#     print datetime.datetime.now()
#
# #一
# # begin(getTime)()
# #二
# getTime()

#
# import datetime
#
# #闭包
# # 修饰函数
# def begin(func):
#     #不定项传参
#     def wrapper(*args,**kwargs):
#         print "现在时间:"
#         func(*args,**kwargs)
#         #    返回闭包
#     return wrapper
# #
# # 装饰器
# @begin
# #取得时间
# def getTime(a,b,c,d):
#     print a,b,c,d
#     print datetime.datetime.now()
#
# #一
# # begin(getTime)()
# #二
# getTime(6,7,8,9)
#


import datetime
#闭包
# 修饰函数
def begin(arg):
    def begin(func):
        #不定项传参
        # 修饰
        def wrapper(*args,**kwargs):
            print arg
            print "现在时间:"
            func(*args,**kwargs)
            #    返回闭包
        return wrapper
    return begin
# 装饰器
@begin('begin')
#取得时间
def getTime(a,b,c,d):
    print a,b,c,d
    print datetime.datetime.now()
#一
# begin(getTime)()
#二
getTime(6,7,8,9)
