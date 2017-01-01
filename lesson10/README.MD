# Lesson 10

## 主要内容
1. `fork`函数基础知识
    - 返回两次, 因为操作系统将当前进程copy了一份, 一次是在父进程中返回, 一次是在子进程中返回
    - 若返回0则为子进程, 否则为父进程, 因为父进程返回当前进程ID, 与getpid返回一致

```python
# --- 多进程 ---
print 'I \'m Process %s' % os.getpid()

pid = os.fork()
if pid == 0:
    print 'I \'m a child process(%s) \
and my parent process is %s' % (os.getpid(), os.getppid())
else:
    print 'I \'m a parent process(%s) \
and my child process is %s' % (os.getpid(), pid)
```
2. `multiprocessing`模块提供了更为简单的方式来创建多进程
3. 多进程通信有多种手段包括Queue, Pipes等来保持同步

```python
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
pr.terminate() # 因为是死循环, 所以需要强制结束
```

4. 如果需要需要使用多进程开发, 推荐使用`Pool`

```python
def long_time_task(name):
    print '%s Hello %s' % (os.getpid(), name)
    time.sleep(5)

p = Pool(4)
for i in range(5):
    p.apply_async(long_time_task, args=(i,))

p.close()
p.join()  # 等进程池中的进程完事儿
print 'all done'
```

## 认知点

