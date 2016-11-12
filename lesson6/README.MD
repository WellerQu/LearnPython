# Lesson 6

## 主要内容

- 模块(Modules)
    - 即文件名, e.g. a.py 即 a
- 包(package)
    - 即目录名, e.g. web/ 即 web
- sys模块
    - sys.argv 获取调用模块时的参数
    - sys.path 模块搜索路径

```
# from <package> import <Module>
from web import a

a.sayHello()
```

- 特殊变量
    - 以__开头和结尾的变量, e.g. __author__ = "nixon"
- 私有(private)描述符
    - 以__开头, 不过这只是一个约定, 并不会被限制调用
- 公开(public)描述符
- 第三方模块
    - 官方推荐的包管理工具是pip, 用法和npm或者glide类似
    - e.g. pip install PIL
- 模块搜索路径
    - 首先搜索当前目录
    - 然后搜索已安装的内置模块和第三方模块, 搜索路径在sys.path中
- 更改模块搜索路径
    - 可以修改sys.path.append('path/to/'), 仅运行时生效
    - 也可以修改PYTHONPATH环境变量, 永久生效
    - 以上两种方式都不会影响python本身的搜索路径

## 认知点

- [ ] moudles
- [ ] package
- [ ] sys模块
- [ ] 特殊变量,私有变量,公开变量
- [ ] 第三方模块
- [ ] 修改模块搜索路径
