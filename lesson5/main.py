#!/usr/bin/env python
# -*- coding: utf-8 -*-
import functools

print "Hello World"

L = map(str, [1, 2, 3])
print L


def counter(a, b):
    return a, b

L = map(counter, [1, 2, 3], (1, 2, 3))
print L


def cSum(a, b):
    return a + b

L = reduce(cSum, [1, 2, 3])
print L


def primeNum(n):
    if n == 2 or n == 3:
        return True
    elif n > 3 and n % 2 != 0 and n % 3 != 0:
        return True
    else:
        return False

L = filter(primeNum, range(1, 101))
print L


def fn():
    def f():
        return 2
    return f

ex = fn()
print ex()

ex1 = fn()
ex2 = fn()
print ex1 == ex2


def retFn():
    return fn

ex3 = retFn()
ex4 = retFn()
print ex3 == ex4


def fn():
    return lambda x: x + x

print fn()(1)

ex5 = fn()
ex6 = fn()

print ex5 == ex6
print fn().__name__


def log(fn):
    def wrapper():
        print 'call %s()' % fn.__name__
        return fn()
    return wrapper


@log
def testFn():
    print 'Hello'

testFn()


# 一个更复杂的装饰器实例
def customLog(text):
    def dec(fn):
        functools.wraps(fn)
        def wrapper():
            print text
            return fn()
        return wrapper
    return dec


@customLog('Hello')
def testFn2():
    print 'yes'

testFn2()


def forPartial(a, b=1, *c, **d):
    return a, b, c, d


fn = functools.partial(forPartial, 2, 3, *(1,2,3), sw=1)
print fn()
