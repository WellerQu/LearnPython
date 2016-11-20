# Lesson 8

## 主要内容

- 动态给类型实例添加属性和方法
    - 这和其他脚本语言一样
    - 别的同类型实例不被影响

```python
class Student(object):
    pass

s1 = Student()
s2 = Student()

s1.age = 12 # 动态添加属性
s1.say_hello = lambda x: x

print s1.age, s1.say_hello(22)
# print s2.age # Error
# print s2.say_hello(22)
```

- 动态给类型添加方法
    - 依赖types包的MethodType模块

```python
Student.say_hello = MethodType(lambda x: x, None, Student)

print s1.say_hello(1), s2.say_hello(2)

# 同样页能给实例添加方法
s1.say_hello = MethodType(lambda x: x + 1, s1, Student)
print s1.say_hello(1)
```

## 认知点

