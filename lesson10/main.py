#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
import time
from multiprocessing import Process, Queue

print 'Lesson %d' % 10

'''
Lesson 10
'''

__author__ = 'Nixon'

# os.getpid, os.getppid
# 前者返回当前进程ID,
# 后者返回当前进程的父进程ID

# --- 多进程 ---
'''
print 'I \'m Process %s' % os.getpid()

pid = os.fork()
if pid == 0:
    print 'I \'m a child process(%s) \
and my parent process is %s' % (os.getpid(), os.getppid())
else:
    print 'I \'m a parent process(%s) \
and my child process is %s' % (os.getpid(), pid)
'''

if __name__ == '__main__':
    q = Queue()

    def w(q):
        for key in ['A', 'B', 'C', 'D']:
            print 'Put a string %s into queue' % key
            q.put(key)
            time.sleep(2)

    def r(q):
        while True:
            value = q.get(True)
            print 'Get a string %s from queue' % value

    pw = Process(target=w, args=(q,))
    pr = Process(target=r, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    pr.terminate()
