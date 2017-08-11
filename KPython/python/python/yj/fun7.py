#!/esr/bin/python
#coding=utf-8
# w=6
# def kk():
#     b=1
#     print b
# kk()
# print w
# print "........"
a=5
b=4
def s():
#声明全局
    global a,b
    a+=1
    b+=1
    print a,b
    c,d=1,2
    #局部以字典输出
  # 返回值
    return locals()
    print fun()
print a
print globals()
