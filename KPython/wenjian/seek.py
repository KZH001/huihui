#coding=utf-8
f = open('file','r+')

s = f.read(6)

 #偏移量
print f.tell()
f.seek(6)
# f.seek(6,1)
# #f.seek(-7,2)
print f.read(6)






f = open('file','a')

In [2]: print >>f,"增加"

In [3]: f.flush()

In [4]: quit
