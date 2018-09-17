a = 3


def func():
    print(a)


func()


# 命名空间
# 依赖倒置原则
def input():
    print('in input now')


input()
# 类似于js的作用域
# 下面这两个是一样的,一个是十进制,一个是十六进制
print(id(input))
print(input)

# 作用域 局部用global声明
a = 1

4


# 对于不可变的数据类型,据不中可以查看全局作用于的变量,但是不能直接修改,如果要修改,要在程序开始添加global声明
def func1():
    global a
    a += 1
    print(a)


func1()
print(a)

# locals globals
a = 1
b = 2


def functest():
    x = 'aaa'
    y = 'bbb'
    # 局部作用域
    print(locals())
    # 全局作用域 全局+内置
    print(globals())


functest()
