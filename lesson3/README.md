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
    - 必选参数
    - 默认参数
        - e.g. def test(x, y=2) ES2015的默认参数应该就是copy的这里.
    - 默认参数应该指向不可变对象, 原因是默认参数在函数定义时就已经计算出来了.
    - 可变参数, 可以传入0个或多个参数, 这些参数将组成一个tuple
        - e.g. def test(*nums)  # nums是一个tuple
    - '*'还可以将一个list类型或tuple类型的数据展开, 以匹配可变参数
    - 关键词参数, 允许传入0个或多个指定参数名的参数, 这些参数将组成一个dict
        - e.g. def test(**kw)   # kw是一个dict
    - 参数组合
        - 同一个函数的参数列表中, 可变参数和关键词参数均仅可出现一次
        - e.g. def test(a, b=1, *nums, **kw)    # a必选参数, b可选参数, nums可变参数, kw关键词参数

```
# 默认参数
def test(a, b=2):
    print a, b

# wrong: default parameters was computed when define
def test(a=[]):
    a.append('End')
    print a

# right
def test(a=None):
    if a is None:
        a = ['End']
    print a

# 可变参数
def test(*num):
    print nums[0], nums[1]

test(*[3, 2, 1])

# 关键词参数
def test(**kw):
    for key in kw:
        print key, kw[key]

test(a=1, b=2)
```

## 认知点

- [x] 调用函数的方式及各类型参数的传递方式
- [x] 在repl环境中如何查看内置函数的帮助信息
- [x] 将函数赋值给一个变量?
- [x] 定义函数及其参数
- [x] 函数的返回值及如何接收返回值
- [x] 必选参数
- [x] 默认参数
- [x] 可变参数
- [x] 关键词参数
- [x] 参数组合
