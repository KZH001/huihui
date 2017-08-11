# coding=utf-8
#文件结构
import os
# 文件时间
import time

filename = raw_input("file name:")

file_stat = os.stat(filename)

print file_stat

print time.localtime(file_stat.st_ctime)
