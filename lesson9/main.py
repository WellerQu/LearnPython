#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

'''
Lesson 9
'''

try:
    import cPickle as pickle
except ImportError:
    import pickle

import json


__author__ = "nixon"


# 读文件
# 将I/O操作包裹在try...except...结构中可以保证程序的健壮性

f = False

try:
    f = open('./a.txt', 'r')
    print f.read()
except IOError as e:
    print e
finally:
    if f:
        print 'close f'
        f.close()


# 写文件

f = False

try:
    f = open('./a.txt', 'w')
    f.write('I\'m Nixon %f' % time.time())
except Exception as e:
    print e
finally:
    if f:
        f.close()


# 上面的写法太啰嗦, 有效避免忘记关闭file-object的问题

try:
    with open('./a.txt', 'w') as f:
        f.write('Happy new year')
except Exception as e:
    print e


# cPickle or Pickle
d = dict(name='nixon', age=12, score=100)
print d

str = pickle.dumps(d)
print str

d = pickle.loads(str)
print d

print json.dumps(d)


class Student(object):
    def __init__(self):
        self.name = "Nixon"
        self.age = 29

stu = Student()
print json.dumps(stu, default=lambda obj: {'name': obj.name, 'age': obj.age})
