# Lesson 5

## 主要内容

- map函数
    - 第一个参数一定是一个函数
    - 第二个参数及以后均为列表
    - 第二个参数及以后将分别逐个传入第一个参数(函数), 这意味着map的参数个数必须比第一个参数(函数)的参数个数多1

```
L = map(str, [1, 2, 3])
print L


def counter(a, b):
    return a, b

L = map(counter, [1, 2, 3], (1, 2, 3))
print L
```

- reduce函数
    - 累计计算
    - reduce(fn, [1, 2, 3]) 相当于 fn(fn(1, 2), 3)
    - fn中每次必须返回结果作为下一次计算的第一个参数

```
def cSum(last, current):
    return last + current

L = reduce(cSum, [1, 2, 3])
print L
```

- filter函数
    - 将判断结果为false的元素过滤掉
    - 判断结果为返回值

```
# 求1到100以内的素数

def primeNum(n):
    if n == 2 or n == 3:
        return True
    elif n > 3 and n % 2 != 0 and n % 3 != 0:
        return True
    else:
        return False

L = filter(primeNum, range(1, 101))
print L
```

- 返回函数
    - 函数内部可以再声明函数, 并将函数作为返回值返回
    - 闭包和javascript一样

```
def fn():
    def f():
        return 2
    return f

ex = fn()
print ex()

ex1 = fn()
ex2 = fn()

print ex1 == ex2
# False
```

- 匿名函数
    - lambda关键词开始一个匿名函数

```
def fn():
    return lambda x: x + x

print fn()(1)
```

- 装饰器
    - 函数也是对象, 通过fn.__name__可以拿到函数的名字
    - 在代码运行期间动态增加功能的方式,称之为"装饰器"
    - 本质上,装饰器就是一个返回函数的高阶函数
    - 通过`@`语法来代理目标函数

```
def decoratorFunc(fn):
    def wrapper():
        // TODO: before fn was executed, add ours logic code
        return fn();
    return wrapper;

@decoratorFunc
def test():
    print "Hello"

# 相当于test = decoratorFunc(test)
```

- 偏函数
    - 偏函数是将所要承载的函数作为partial()函数的第一个参数，原函数的各个参数依次作为partial()函数后续的参数，除非使用关键字参数。
    - 用于秃顶函数的某些参数

## 认知点

- [ ] map
- [ ] reduce
- [ ] filter
- [ ] 函数作为返回值
- [ ] 匿名函数
- [ ] 装饰器
- [ ] 函数名获取,functools的作用
- [ ] 偏函数
