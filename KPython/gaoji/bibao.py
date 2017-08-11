# coding=utf-8
# 闭包   变量保护
# 定义函数
def out():
    # 外层函数定义自由变量
    a = 1
    # 嵌套函数
    def inner():
        # 输出自由变量
        print a
        print "I'm inner"
    # 返回闭包
    return inner
# 嵌套函数
f = out()
f()
