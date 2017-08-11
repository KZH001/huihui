#coding=utf-8
class Magic1(object):
    def __init__(self):
        #实例化对象自动执行
        print "__init__..."

    def __new__(cls):
        print "__new__.."
        # 调用父类 返回一个值传给__init__
        return super(Magic1,cls).__new__(cls)
            # 当类的实例化对象带有参数时自动调用
    def __call__(self,a):
        # print "__call__"
        print a
            # 销毁时执行
    def __del__(self):
        print "__del__...."

m = Magic1()
m("kang")

del m
print "over"
