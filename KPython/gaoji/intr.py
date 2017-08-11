#coding=utf-8

# 内键函数
# 判断对象名字   获取属性  设置属性  删除属性   判断对象      判断子类
#hasattr  getattr  setattr  delattr  isinstance   issubclass

#类的属性方法不可删
class Parent(object):
    name = 'Kang'

class Child(Parent):
    pass

q = Parent()
print issubclass(Child,Parent)
print isinstance(q,Parent)

print "+++++++++"

print hasattr(q,'name')

print getattr(q,'name')

#setattr(q,'age',23)

q.age = 23

delattr(q,'age')

#print q.age
