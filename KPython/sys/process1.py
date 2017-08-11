#!/usr/bin/python
#coding=utf-8
#进程池
# 查看方法
# print (dir (multiprocessing))
# 模块有个类
import multiprocessing
from time import sleep
import os


def worker(msg):
    print os.getpid()
    while True:
        sleep(2)
        print msg
    return

# 创建启动进程 名字  参数
if __name__ == '__main__':
    # 线程值
    p = multiprocessing.Pool(processes = 4)
    result = []
    # 方法
    for i in xrange(10):
        msg = "hello %d"%(i)
        # 加入线程池
        result.append(p.apply_async(worker,(msg,)))

    for res in result:
        print res.get()
