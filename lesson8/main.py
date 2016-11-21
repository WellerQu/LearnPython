#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType


class Student(object):
    pass

s1 = Student()
s1.age = 12
s1.say_hello = lambda x: x

print s1.age
print s1.say_hello(1)

s2 = Student()
# Error
# print s2.age
# print s2.say_hello(2)


def set_age(self, age):
    self.age = age


def get_age(self):
    return self.age

s1.set_age = MethodType(set_age, s1, Student)
s1.get_age = MethodType(get_age, s1, Student)

s1.set_age(13)
print s1.get_age()


Student.get_age = MethodType(get_age, None, Student)
Student.set_age = MethodType(set_age, None, Student)

s2.set_age(15)
print s2.get_age()


class Teacher(object):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
