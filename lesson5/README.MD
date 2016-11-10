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


## 认知点

- [ ] map
- [ ] reduce
- [ ] filter
- [ ] 函数作为返回值
