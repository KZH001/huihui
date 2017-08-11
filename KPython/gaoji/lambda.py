# coding=utf-8
# 匿名函数
           #幂次方
Q = [lambda x:x ** 2,
     lambda x:x ** 3,
     lambda x:x ** 4]

for q in Q:
    print(q(2))
