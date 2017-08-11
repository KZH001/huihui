# coding=utf-8
# python3
# 全局变量
a = 1
# 定义函数
def out():
    # 函数内定义局部变量
    b = 2
   # 函数内嵌套函数
    def inner():
        #  关键字  作用域  相当于单层函数的global全局变量
        nonlocal b
           #循环
        b += 1
        print (b)
    inner()

out()
