#coding=utf-8

#静态方法

# class TestStaticMethod(object):
#     @staticmethod
#     def foo():
#         print "calling atatic method foo()"
#
#             # 静态方法
#     # foo = ataticmethod(foo)
#
# class Child(TestStaticMethod):
#     pass
#
# Static = TestStaticMethod()
#
# Static.foo()
# TestStaticMethod.foo()
#
# child = Child()
#
# child.foo()


print "++++++++++"
class TestClassMethod(object):
    @classmethod
    def foo(cls):
        print "calling class method foo()"
        print cls.__name__

class Child1(TestClassMethod):
    pass

cls = TestClassMethod()

cls.foo()
TestClassMethod.foo()

child = Child1()
child.foo()
