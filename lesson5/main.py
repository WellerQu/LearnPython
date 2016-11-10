#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
