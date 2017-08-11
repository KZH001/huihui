#!usr/bin/python
#coding=utf-8
#进程临界资源管理
import multiprocessing
import time

def wait_for_event(e):
    print 'wait_for_event:starting'
# 等待（阻塞）
# set之后运行
    e.wait()
    print 'wait_for_event:e.is_set()->',e.is_set()

def wait_for_event_timeout(e,t):
    print 'wait_for_event_timeout:starting'
# 超过时间
    e.wait(t)
    print 'wait_for_event_timeout:e.is_set()->',e.is_set()

if __name__ == '__main__':
    e = multiprocessing.Event()

    w1 = multiprocessing.Process(name = 'block',target = wait_for_event,args = (e,))
    w1.start()

    w2 = multiprocessing.Process(name = 'non-block',target = wait_for_event_timeout,args = (e,2))
    w2 .start()

    print 'main : waiting before calling Event.set()'
    time.sleep(4)
    e.set()
    print 'main:event is set'
