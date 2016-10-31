#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = 1
b = -1

if (abs(a) == abs(b)):
    print u'是的, a的绝对值等于b的绝对值'

myAbs = abs

if (myAbs(a) == myAbs(b)):
    print u'是的, myAbs也与abs有同样的功能'


def testWithoutParams():
    print u'无参数函数'


def testWithDefaultParams(a=1):
    print u'a默认就是', a


def testChangableParams(*a):
    print u'可变参数', a, len(a)


def testKeyParams(**kw):
    print u'关键词参数', kw


def testComposeParams(a, b=1, *num, **kw):
    print u'组合各种参数', a, b, num, kw


testWithoutParams()
testWithDefaultParams()
testChangableParams(1, 2, 3, 4)
testChangableParams(*[1, 2, 3])
testChangableParams(*(1, 2,))
testKeyParams(city=1)
testComposeParams(1, 5, *(3, 3), city=1)


def testReturnValue():
    return 1, 2

x, y = testReturnValue()
print x, y
