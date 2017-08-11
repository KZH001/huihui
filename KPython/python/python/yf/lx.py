'''
#!/usr/bin/python
#coding=UTF-8
a = 21
b = 10
c = 0
c = a + b
print "1 - c 的值为：",c
c = a - b
print "2 - c 的值为：",c
c = a * b
print "3 - c 的值为：",c
c = a / b
print "4 - c 的值为：",c
c = a % b
print "5 - c 的值为：",c
python 1.py
a=2
b=3
c=a**b
print "6 - c 的值为:",c
print("........")
#!/usr/bin/python
#coding=UTF-8
print "您好，世界"

print "Hello!"
print("......")
if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    print "False"

total = inme_one + \
        inme_two + \
        inme_three
print(".....")
raw_input("\n\nPress the enter key to exit.")

import sys; x = 'runoob'; sys.stdout.write(x + 'n')
print("...")
# !/usr/bin/python
# coding=UTF-8
x = "a"
y = "b"
print x
print y
print '---'
print x,
print y,

if expression :
    suite
elif expression :
    suite
else :
    suite
print(".....")
# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
import sys
print '参数个数为:', len(sys.argv), '个参数。'
print '参数列表:', str(sys.argv)
python 1.py  kk
print("........")
# #!/usr/bin/python
# #coding=UTF-8
counter = 100
milles = 100.0
name = "kang"
print counter
print milles
print name

a = b = c = 1
a,b,c=11,2,"kang"
print (a)
print (b)
print (c)
print("........")
# #!/usr/bin/python
# #coding=UTF-8
str='Hello world!'
print str
print str[0]
print str[2:5]
print str[2:]
print str * 2
print str + "TEST"
print("........")
# #!/usr/bin/python
# #coding=UTF-8
# list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
# zeng = [123, 'john']
# print list
# print list[0]
# print list[1:3]
# print list[2:]
print("........")
# #!/usr/bin/python
# #coding=UTF-8
# dict = {}
# dict['one'] = "this is one"
# dict[2] = "This is two"
# tinydict = {'name': 'kang','zeng':5656, 'dapt': 'hui'}
# print dict['one']
# print dict[2]
# print tinydict
# print tinydict.keys()
# print tinydict.values()
print("........")

# l = []
#
# type(l)
#
# l=[1,2,3,4,5]
#
# l=[1,2,3,4,'k']
# a=1
# l=[a,[2,3,5],4,'k']
 # l[0]
# l[1][2]=30
# print l[1][2]
# l=[1,4,3,2,5,6,7]
# l.append(8)
# l.count(3)
# print l.count(3)
# l.extend([5,6,7,8])
# l.index(3)
# print l.index(3)
# l.insert(2,100)
# print l
# l.pop(4)
# print l
# l.remove(6)
# print l
# l.reverse()
# print l
# l.sort()
# print l
# def cmp(x,y):
#  return y - x
# l.sort(cmp=cmp)
# print l
print("........")
'''
t = ()
t = (1)
type(t)
print type(t)

t = (1,)
t = (1,2)
type(t)
print type(t)

l=[1,2,45,85]
max/min(l)

l=[1,2,3,4,5,6]
l1=l
l1[0]=100
print l1
print l
l=[1,2,3,4,5,6]
l1=l[:]
l1[0]=100
print l1
print l

import copy
k=[1,2,3,[1,2,3]]
k1=copy.copy(k)
k2=copy.deepcopy(k)
k1[1]=100
k2[3][2]=200
print k
print k1
print k2

k=(1,2,3,[4,5,6])
k[3][2]=3
print k

l='  hello '
l.strip()
print l
s='nihao{1},kang{0}'.format('one','two')
print s

str = "1,2,3,4,5,6/"
print str.rsplit("3,4")
