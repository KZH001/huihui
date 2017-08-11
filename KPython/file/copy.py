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
