# Lesson 8

## 主要内容

- 动态给类型实例添加属性和方法
    - 这和其他脚本语言一样
    - 其它的同类型实例不被影响

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

- `type()`动态创建类
    - 依次传入类名, 继承类元组, 方法映射

```python
Master = type('Master', (object,), dict(say=lambda self, x: 'Hello %s' % x))
m = Master()
print m.say('world')
```

- 元类MetaClass
    - 自定义MetaClass必须继承type
    - 自定义MetaClass需要实现`__new__`方法, `__new__`方法的参数依次是:
        1. 创建类的对象
        2. 类的名字
        3. 父类集合
        4. 方法集合
    - 将元类赋予当前创建类的`__metaclass__`特殊变量

```python
class MyClassMeta(type):
    def __new__(cls, className, bases, attrs):
        attrs['say'] = lambda self, x: 'Hello %s' % x
        return type.__new__(cls, className, bases, attrs)

class MyClass(object):
    __metaclass__ = MyClassMeta

m = MyClass()
print m.say('World');
```

- ORM

## 认知点

