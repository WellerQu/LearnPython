# Lesson 2

## 主要内容

- **#** 表示注释, 和其他编程语言的注释一样, 解释器会忽略本行
- 基础数据类型
    - 整数 e.g. 123, 0xff00
        - 整数除法结果永远是整数(精确运算)
        - 0 是一个假值, 且 `0 is False` 返回真
        - 字符串类型转换为数字类型int(str)
    - 浮点数 e.g. 1.23, 1.23e9
        - 运算存在四舍五入的误差
    - 字符串 e.g. 'Hello World'
        - 多行'''多行文本'''
    - 布尔值 e.g. True / False
        - and, or, not 表示**与,或,非**
    - 空值 None, None 不等于 0
        - None 是一个假值, 且 `None is False` 返回真
- 变量支持隐式申明, **大小写敏感**, 全局作用域
- 实际上Python里面并没有常量, 一个依赖约定的做法的, 用全部大写的单词表示常量
- Python用u'中文'来表示Unicode编码. e.g. u'中文'
    - 在repl环境中可以直接用`print u'中文'`
    - 在脚本文件中, 除了要在中文前添加`u`, 需要在开头声明文件内容编码格式
    
```python
#!/usr/bin/env python
# -- coding: utf-8 --
```

- 字符串格式化, 与C语言是一致的, 使用`%`来提供实际数据, 例如

```python
>>> 'Hello, %s' % 'World' # 单个占位符
>>> 'Hello, %s, %s' % ('Nixon', 'World, 'World') # 多个占位符需要使用括号
```

- 常见的占位符:
    - %d 整数
        - %f 浮点数
        - %s 字符串
        - %x 十六进制整数
    - 格式化整数和浮点数还可以指定是否补齐0或者保留的小数位数
        - %和字母之间插入数字表示**场宽**, 不够长度右对齐, e.g. 'A%2d' % 1 # 输出 A 1, 注意A和1之间存在一个空格
        - 左补齐0, e.g. 'Age is %02d' % 1 # 输出Age is 01
        - 保留2位小数, e.g. 'Money is %.2f' % 3.1415926 # 输出Money is 3.14
    - 转换编码格式 e.g. u'中文'.encode('gb2312')
- Python的内置数据类型list
    - 和JavaScript的数组一样 e.g. `['a', 'b', 'c']`
    - 通过下标访问list元素, 有意思的是, 下标-1可以访问最后一个元素, 依次类推, -2访问倒数第二个元素. 但是无论顺数或倒数, 都不能越界.
    - list的方法
        - append(n)     末尾追加
        - insert(i, n)  指定位置插入
        - pop(i)        删除末尾或指定位置的元素
        - len(list)     获得长度
        - sort()        排序

```
>>> ls = ['abc', '123', 444]
>>> ls[0] # 输出 'abc'
>>> ls[2] # 输出 444
>>> ls[-1] # 输出 444
```

- Python的内置数据类型tuple
    - 使用`()`来初始化. e.g. t = (1, 2, 3)
    - 更重要的是, **tuple元组不可变**, 其他和list访问起来一致
    - tuple很简单, 但使用时仍然有一些小技巧

```python
# 初始化一个空的tuple
t = ()

# 初始化仅有一个元素的tuple
t = (1,)
# 注意, 1后面必须有一个',', 否则等价于t = 1, 就不是元组了
```

- 循环

```python
for key in []:
    # TODO: add code

while condition:
    # TODO: add code

# 值得注意的是, 循环和if语句一样, 有一个':'存在.
```

- range函数, 提供生成[0, n)区间的整数序列
- Python内置数据类型dict字典
    - 初始化dict就像JavaScript中初始化一个JSON对象一样, 而且数据读写方式也是一样
    - 就连是否包含特定键值的判断也是一样

```python
dt = {'A': 100, 'B': 101: 101}
print dt['A']

dt['B'] = 102
print dt

print 'C' in dt, 'A' in dt
# in 返回一个Boolean类型数据
```

- Python内置数据类型set集合
    - 初始化一个set需要以一个list作为输入
    - set中仅存储key, 没有value
    - set中的key不会重复, 可以看成数学上无序和无重复的元素集合
    - 可用的方法
        - add(key)      添加key
        - remove(key)   移除key

```python
ls = [1, 2, 3, 3]
s = set(ls);

print s
```


## 认知点
- [x] 如何注释一行代码?
- [x] 有多少中基础数据类型?
- [x] 多行字符串如何表示?
- [x] 0, None, False之间的异同?
- [x] 使用中文?
- [x] 转换字符串编码?
- [x] 格式化字符串
- [x] 场宽是啥?
- [x] 内置类型list及其方法
- [x] 内置类型tuple及其特性
- [x] 判断和循环?
- [x] range函数?
- [x] 内置类型dict及其方法
- [x] 内置类型set及其方法

## Otherwise

dict是允许一个变量作为key的

```python
a = 1
dt = {a: 1}
print 'a' in dt # False
print a in dt   # True

dt = {'a': 1}
print 'a' in dt # True
```
