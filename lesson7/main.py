#!/usr/bin/env python
# -*- coding: utf-8 -*-

import types

from mo import student
from ol import teacher

print "Hello World"

stu = student.Student("nixon", 28)
print stu.getName()
print stu.age
print '仍然可以访问: %s' % stu._Student__name

tea = teacher.Teacher("nixon", 28)
print tea.getAge()


class GoodStudent(student.Student):
    def __init__(self, name):
        student.Student.__init__(self, name, 0)
        # super(student.Student, self).__init__()


gs = GoodStudent("ming")
print 'GoodStudent\'s name is %s' % gs.getName()

# print type('123') == types.StringType
print isinstance('123', types.StringType)
