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

## 认知点
