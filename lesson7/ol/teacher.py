#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
teacher class
'''


class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        return self.age
