# 空洞文件
f = open('hold','w')

f.write('b')
f.seek(1024*1024*3)
f.write('e')

od -c hold
