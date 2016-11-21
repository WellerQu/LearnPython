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

- 可限制动态赋予对象属性的特殊变量
    - 赋予__slot__特殊变量一个元组

```python
class Student(object):
    # 赋予元组
    __slot__ = ('name', 'age')
```

- 使用@property装饰器
    - @property用于读方法
    - @property会生成另外一个@propertyName.setter的装饰器给写方法
    - 访问属性不再依赖setter, getter方法
    - 没有只写属性, 只有只读属性(仅有@property装饰的函数)

```python
class Teacher(object):
    # 读属性
    @property
    def name(self):
        return self._name;

    # 写属性
    @name.setter
    def name(self, name):
        self._name = name;

    # 只读属性, 因为没有setter
    @property
    def age(self):
        return self._age;
```

## 认知点

- [ ] 可以动态的给对象实例赋予新的属性, 不同实例间没有影响
- [ ] 可以动态的给对象实例赋予新的方法, 不同实例间没有影响
- [ ] 可以给类型赋予新的方法, 同类型的不同实例均受影响
- [ ] `@property`属性读装饰器
- [ ] `@propertyName.setter`属性写装饰器
