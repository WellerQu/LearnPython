#!/usr/bin/env python
# -*- coding: utf-8 -*-

from web import a
import sys

a.sayHello()

print 'main', __name__
print sys.argv

print '--------'
# print a.__builtins__
print '__doc__: %s' % a.__doc__
print '__file__:%s' % a.__file__
print '__name__:%s' % a.__name__
print '__package__:%s' % a.__package__
print '__author__:%s' % a.__author__
