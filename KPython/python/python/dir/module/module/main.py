#!/usr/bin/python
#coding=utf-8
#导入模块
# import module1
# # from 模块名 import 变量名
# #重新载入  内置函数
# reload(module1)
#
# print module1.a
# obj=module1.A()
# obj.a()
# module1.b()
# #文档
# print module1.__doc__
#
import module1
from module2 import D,b
#重新载入  内置函数
reload(module1)

print module1.a
obj=module1.A()
obj.a()
module1.b()
#文档
print module1.__doc__

obj_d=D()
obj_d.d()
print b
