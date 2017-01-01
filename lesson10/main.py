#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
# from multiprocessing import Process, Queue
from multiprocessing import Pool

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

# --- 通过队列来同步多个进程 ---
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
'''

# --- Pool ---
if __name__ == '__main__':
    def long_time_task(name):
        print '%s Hello %s' % (os.getpid(), name)
        time.sleep(5)

    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    p.close()
    p.join()  # 等进程池中的进程完事儿
    print 'all done'
