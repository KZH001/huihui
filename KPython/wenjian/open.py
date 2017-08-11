# coding=utf-8
try:
    f = open('file1','w')
except IOError as e:
    print e

print f

f.close()
print f

#生成一个对象 执行完之后自动销毁
with open('file','r') as f:
    for i in f:
        print i,
