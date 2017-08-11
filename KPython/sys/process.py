#!/usr/bin/python
#coding=utf-8
# 查看方法
# print (dir (multiprocessing))
# 模块有个类
import multiprocessing
from time import sleep
import os


def worker(sec):
    print "parent pid:",os.getppid()
    while True:
        sleep(sec)
        print "worker..."
    return

# 创建启动进程 名字  参数
if __name__ == '__main__':
    p = multiprocessing.Process(target = worker,name = "myprocess",args = (3,))
    p.start()
    print os.getpid()
