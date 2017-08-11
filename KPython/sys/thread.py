#!/usr/bin/python
#coding=utf-8
# 创建线程
from time import ctime,sleep
import threading

#函数 线程名
def music(name):
    print('I was listening to music %s . %s'%(name,ctime()))
    sleep(2)

def move(name):
    print('I was at the movie %s! %s'%(name,ctime()))
    sleep(5)
# 定义列表
threads = []
# 生成值
t1 = threading.Thread(target = music,args = ('bady',))
t2 = threading.Thread(target = move,args = ('afanda',))

threads.append(t1)
threads.append(t2)

if __name__ == '__main__':

    for t in threads:
        t.setDaemon(True)
        t.start()

    # 线程结束时收集
    for t in threads:
        t.join()

    print("all over %s"%ctime())
