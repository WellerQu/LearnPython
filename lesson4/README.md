# Lesson 4

## 主要内容

- 切片
    - 从列表中复制出任意片段, 故名"切片"
    - 语法: ls[i:j:k]
        - i 表示从第几个索引开始(含), 如果缺省, 则默认为列表开头, i = 0
        - j 表示到第几个索引结束(不含), 如果缺省, 则默认为列表长度, j = len(ls)
        - k 表示间隔多少个元素, 如果缺省, 则默认为0, 无间隔, k = 0
    - e.g. ls[:] 复制一个完整列表
    - e.g. ls[1:4] 复制索引[1:4)区间的3个元素
    - e.g. ls[:4] 复制索引[0,4)区间的4个元素
    - e.g. ls[1:] 复制从索引1开始(含), 到末尾的所有元素
    - e.g. ls[::5] 复制从索引0开始(含), 从0+1开始(不含)间隔5个
    - e.g. ls[-1:] 复制从索引len(ls) - 1开始(含), 向右取值到末尾
    - e.g. ls[-2:-1] 复制从索引len(ls) - 2开始(含), 向右取值到len(ls) - 1(不含)
    - tuple也是列表, 也可以切片
    - 字符串也是列表, 也可以切片

- 迭代
    - 通过`for...in...`来完成, 作用于可迭代对象, 包括但不限于list, tuple, dict
        - e.g. for key in dict                  # 遍历dict的key
        - e.g. for value in dict.itervalues()   # 遍历dict的value
        - e.g. for k, v in dict.iteritems()     # 同时遍历dict的key和value
        - e.g. for ch in 'ABC'                  # 遍历字符串中的每一个字符
    - 判断一个对象是否是可迭代对象, 方法是通过collections模块的Iterable类型判断
    - 类似Java那样的下表循环需要用到内置函数enumerate, 可以把一个list变成索引-元素对

```
from collections import Iterable
if isinstance(obj, Iterable):
    print u'是一个可迭代对象'
```

```
for index, value in enumerate(['A', 'B', 'C']):
    print index, value

# 另外一种常见的写法
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y
```

- 列表生成式
- 生成器

## 认知点

## otherwise

- '==' 判断值是否相等, 而非指针地址
