#!/usr/bin/env python

print 'Hello', 'World'

print 'How old are you?'
age = int(raw_input())

if age > 20:
    print 'more than 20'
elif age == 20:
    print 'equals 20'
else:
    print 'less than 20'
