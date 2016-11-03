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
