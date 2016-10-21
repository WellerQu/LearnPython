#!/usr/bin/env python
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

if None == False:
    print 'None equals to False'

if 0:
    print '0 is a True'
else:
    print '0 is a False'

if 0 == False:
    print '0 equals to False'
