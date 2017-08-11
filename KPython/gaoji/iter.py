# coding=utf-8
# 生成可迭代关系
class TestIter(object):
    def __init__(self,a):
        self.a = a
        # 生成可迭代对象
    def __iter__(self):
        return self
        # 生成可迭代关系
    def next(self):
        self.a += 1
        if self.a > 10:
            raise
        return self.a ** 2

n = TestIter(2)
print n.next()
print n.next()
print n.next()
print n.next()
