# # coding=utf-8
# class A(object):
#     #不存在属性可获取属性有则报错
#     def __getattr__(self,name):
#         print "You use getattr"
#         return "NO"
#        #不存在时课设置属性
#     def __setattr__(self,name,value):
#         print "You use setattr"
#         self.__dict__[name] = value
#
#
# a = A()
#
# print a.k
# a.x = "set x"


class A(object):
    #不存在属性可获取属性有则报错
    def __getattr__(self,name):
        print "You use getattr no attr %s"%name
        return "NO"
       #不存在时课设置属性
    def __setattr__(self,name,value):
        print "You use setattr"
        self.__dict__[name] = value

    def __delattr__(self,name):
        print "You use delattr"

a = A()

print a.k
a.x = "set x"
