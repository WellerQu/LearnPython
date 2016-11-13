#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
student class
'''

__author__ = "nixon"


class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.age = age

    def getName(self):
        return self.__name
