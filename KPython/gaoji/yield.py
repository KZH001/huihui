# coding=utf-8
#生成器
#         最大
# def fib(max):
    #   定义a，b值
#     a,b = 0,1
    # while 判断
#     while a < max:
            # 生成a
#         yield a
            #  循环
#         a,b = b,a + b
#
# for i in fib(20):
#     print(i)

# def fun(q):
#     a,b = 0,1
#     while a < q:
#         yield a
#         a,b = b,a + b
# for i in fun(21):
#     print(i)

def fab(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a + b
        n = n + 1

for n in fab(5):
    print n
