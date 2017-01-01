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

## 认知点

