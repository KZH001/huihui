# coding=utf-8
#拷贝
# f = open('文件名',‘r’)
# f1 = open('路径','w')
# for i in f:
#     f1.write(i)


try:
    f = open('a.png','r')
    f1 = open('/home/linux/KPYTHON/a.png','w')
except:
    print "open failed"

while True:
    s = f.read(12)
    if not s:
        break
    f1.write(s)
