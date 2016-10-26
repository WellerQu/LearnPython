#!/usr/bin/env python
# -- coding: utf-8 --

n = abs(-1)
print n


def test():
    return 1, 2

x, y = test()
print x + y


def testWithDefault(a, b=2):
    print a, b

testWithDefault(1)
testWithDefault(1, 3)


# don't write like this:
def testWrong(L=[]):
    L.append('End')
    print L

testWrong()
testWrong()


def testRight(L=None):
    if L is None:
        L = ['End']
    print L

testRight()
testRight()


def testWillChangeParam(*nums):
    for key in nums:
        print key

testWillChangeParam(1, 2, 3)

L = [3, 3, 1]
testWillChangeParam(*L)
testWillChangeParam(*[4, 2, 1])
testWillChangeParam(*(5, 5))


def testKWParam(**kw):
    print kw
    for key in kw:
        print key, kw[key]

testKWParam(a=1, b=2)


def testAll(a, b=2, *c, **d):
    print a, b, c, d

testAll(1)
testAll(1, 3)
testAll(1, 3, *(1, 2))
testAll(1, 3, *(1, 1), city=123)
