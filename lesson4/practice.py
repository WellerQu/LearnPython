#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Iterable

print isinstance([], Iterable)


ls = [1, 2, 3]
for index, value in enumerate(ls):
    print index, value


ls = [x for x in range(1, 11)]
for x in ls:
    print x


ls = (x for x in range(0, 11))
print ls.next()

for x in ls:
    print x


def gen():
    yield 99


for x in gen():
    print x
