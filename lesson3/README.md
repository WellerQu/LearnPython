# Lesson 3

## 主要内容
- 调用函数abs, cmp, int, float, str, unicode, bool
- 可以在repl环境中查看函数帮助 e.g. help(abs)
- 函数地址赋值

```
a = abs
print a(-1)
```

- 定义函数关键词: def
    - pass用来做函数体表示函数什么也不做
    - 函数默认返回None

```
def myFunc():
    pass
```

- 内置函数isinstance(t, tuple)
- 抛出错误 e.g. raise TypeError('Hello')
- 允许返回多个值

```
def test():
    return 1, 1

x, y = test()

print x + y
```

- 函数的参数
    - 默认参数 e.g. def test(x, y=2) ES2015的默认参数应该就是copy的这里.
    - 默认参数应该指向不可变对象, 原因是默认参数在函数定义时就已经计算出来了.
    - 可变参数 e.g. def test(*nums) nums是一个tuple
    - '*'还可以将一个list类型的数据展开, 以匹配可变参数

```
```

    - 关键词参数

- 递归函数

## 认知点
