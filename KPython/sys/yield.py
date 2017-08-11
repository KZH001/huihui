#!/usr/bin/python

import time
import sys

# 生产者
def produce(l):
    i = 0
    while True:
        if i < 5:
            l.append(i)
            yield i
            i += 1
            time.sleep(1)
        else:
            return

# 消费者
def consume(l):
    p = prodece(l)
    while True:
        try:
            p.next()
            while len(l) > 0:
                print l.pop()
        except StopIteration:
            sysy.exit(0)

l = []
consume(l)
