#!/usr/bin/env python
# -- coding: UTF-8 --
# this is a comment

a = int(raw_input('input number:'))

if a > 100:
    print 'More than 100'
elif a == 100:
    print 'equals 100'
else:
    print 'Less than 100'

if True:
    c = 21

print c

b = 12
c = 5
print b / c

b = 12.0
c = 5
print b / c

print '''multi line
Hello
World'''

if None:
    print 'None is a True'
else:
    print 'None is a False'

if None is False:
    print 'None equals to False'

if 0:
    print '0 is a True'
else:
    print '0 is a False'

if 0 is False:
    print '0 equals to False'

print u'中文'

print u'你好, %s, 你是不是有$%d美元?' % ('nixon', 10000)

print u'中文'.encode('gb2312')

classmates = ['nixon', 'wangming', 'fengshuang']
print classmates, len(classmates), classmates[1]

t = (1, 2)
print t

for name in classmates:
    print name

sum = 0
for item in range(0, 101):
    sum += item

print sum

dt = {'A': 100, 'B': 100}
print dt, dt['A']

dt['B'] = 102
print dt

print 'C' in dt, 'A' in dt

s = set([1, 2, 3, 3])
print s

s = set((1, 2, 3, 3))
print s
