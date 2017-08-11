#!/usr/bin/python
#coding=utf-8
# 人为异常
#声明类     基于父类
class MyError(Exception):
    pass
    # 定义变量
s = raw_input()
try:
    #检测错误执行错误
    if s == "error":
        print "This is my error"
        # 人为抛出异常
        raise MyError("kkk")
        #无异常直接执行输出内容
    else:
        print s
except MyError as e:
    print "Error message:"
    print (e)

    class MyError(Exception):
        pass
        # 定义变量
    s = raw_input()
    try:
        #检测错误执行错误
        if s != "error":
            print "This is my error"
            # 人为抛出异常
            raise MyError("kkk")
            #无异常直接执行输出内容
        else:
            print s
    except MyError as e:
        print "Error message:"
        print (e)
