#!/usr/bin/python
#coding=utf-8
def div(a,b):
#捕获异常
    try:
# 语句块
        return a /b
# 异常处理语句     类型       生成具体错误内容
    except TypeError as e:
        return e
    #显示语句
        return "kang"
result = div(5,{1})
print result

def k(a,b):
    #捕获错误
    try:
        # 语句块
        c=a/b
# 解决异常语句   错误类型
    except TypeError as e:
        # 生成响应错误
        return e
        # 无异常
    else:
        print "else......"
        # 执行完输出
    finally:
        print "finally....."
    return c
z=k(2,{1})
print z
