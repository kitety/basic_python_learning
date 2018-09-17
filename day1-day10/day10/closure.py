from urllib.request import urlopen


# 引入方法放在开头
def outer():
    a = 1

    # 闭包
    def inner():
        print(a)

    inner()
    print(inner.__closure__)
    # <cell at 0x00000191EA5585E8: int object at 0x0000000055C36C40>,)
    # 有cell才是闭包


outer()
print(outer.__closure__)


# 闭包的返回
def func():
    a = 1

    def func2():
        print(a)

    return func2


a = func()
a()

# js的闭包和py的闭包一模一样!

# import urllib # 引入模块
# 引入方法
# 从...引入...方法


# ret = urlopen('http://www.xh100.cc/').read()
# print(ret)
def get_url(url):
    ret = urlopen(url).read()
    return ret


print(get_url('http://www.xh100.cc/'))
