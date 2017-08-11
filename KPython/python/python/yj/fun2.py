# #!/usr/bin/python
# #coding=utf-8



# def fun(a):
#     a[1] = 1000
#     print a
#     print id(a)
#
# l = [1,2,3,4]
#
# l1 = l[:]
#
# fun(l1)
#
# print "========================="
# print id(l)
#
# print l

def fun(a):
    a[1]=10
    print a
    print id(a)
k=[1,2,3,4]
k1=k[:]
fun(k1)
print "..."
print id(k)
print k
