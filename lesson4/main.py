#!/usr/bin/env python
# -- coding: utf-8 --

ls = ['a', 'b', 'c', 'd', 'e', 'f']
print ls[:]
print ls[1:4]
print ls[:4]
print ls[2:]
print ls[::5]
print ls[-1:]
print ls[-2:-1]

if ls == ls[:]:
    print u'相等'

a = ls[:]
a[0] = 0

print a, ls