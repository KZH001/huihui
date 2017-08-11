#!/usr/bin/python
#coding=utf-8

import dir2.module1
from dir2 import module2

print dir2.module1.a
obj=dir2.module1.A()
obj.a()
dir2.module1.b()
#文档
print dir2.module1.__doc__

kk=module2.D()
kk.d()
print module2.b
