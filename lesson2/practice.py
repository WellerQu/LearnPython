#!/usr/bin/env python
# -- coding: utf-8 --

# 基础数据类型
a = 1
b = 0xFF
c = 1.12
d = 2e-4
e = True
f = None
g = "Hello"

print a, b, c, d, e, f, g

PI = 3.141592627

print PI

print u'这里是中文'

print '%d, %x, %5.3f, %f, %s, %s, %s' % (a, b, c, d, e, f, g)
print '%06.2f' % PI

ls = [1, 2, 'abc']
print ls, ls[2]

ls.append(3)
print ls

ls.insert(2, 'hello')
print ls

ls.pop()
print ls

ls.pop(0)
print ls

print len(ls)

t = (1, )
# t[0] = 2

print t
