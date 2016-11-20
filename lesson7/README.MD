# Lesson N

## 主要内容

- 类
    - 通过class关键词创建
    - __init__为构造函数
    - 没有this指针, 但是有self, 类方法的第一个参数, 可视为this的替代
    - 不支持方法重载
    - 私有变量以'__'开头, 以限制外部访问
    - 创建类时,如果没有合适的类可以继承,就继承object类

ps. 不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量

```
class Student():
    # 构造函数
    def __init__(self, age, name):
        self.age = age
        self.__name = name

    def getAge(self):
        return self.age

stu = Student(12)
stu.getAge()

# 强烈不建议这么做
print stu._Student__name
```

- 继承
    - 调用父类构造函数:
        - 方法一: `Student.__init__(self)`
        - 方法二: `super(Student, self).__init__()`
    - 方法二无法使用带有参数的构造函数

- 多态
    - 与其他面向对象语言中的多态相同

- 获取对象信息
    - type()函数, 可以用来获取基本类型,函数,类的类型
    - `import types` 导入类型定义常量
    - 判断一个变量是否属于某个类型, 优先使用isinstance()函数

```
import types
print type('123') == types.StringType
```

## 认知点

