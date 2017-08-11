# coding=utf-8
import sys

with open('file1','r+') as f:
    print >>f,"光芒万丈，魅力演说"

# 标准输入 在所传输文件显示内容
# print >>sys.stdin,"光芒万丈，魅力演说"
# 标准输出在终端输出内容
# print >>sys.stdout,"光芒万丈，魅力演说"
#标准出错
# print >>sys.stderr,"光芒万丈，魅力演说"
