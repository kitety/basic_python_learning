import os
from urllib.request import urlopen

# 1.编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件），
# 要求登录成功一次，后续的函数都无需再输入用户名和密码
FLAG = False


def login(func):
    def inner(*args, **kwargs):
        global FLAG
        '''登录'''
        if FLAG:
            ret = func(*args, **kwargs)
            return ret
        else:
            username = input('username:')
            password = input('password:')
            if username == 'boss' and password == '123123':
                FLAG = True
                ret = func(*args, **kwargs)
                return ret
            else:
                print('登录失败')

    return inner


@login
def shoplist_add():
    print('增加商品')


@login
def shoplist_del():
    print('删除商品')


# shoplist_add()
# shoplist_del()


# 编写装饰器，为多个函数加上记录调用功能，要求每次调用函数都将被调用的函数名称写入文件
def log(func):
    def inner(*args, **kwargs):
        with open('log', 'a', encoding="utf-8") as f:
            f.write(func.__name__ + '\n')
        ret = func(*args, **kwargs)
        return ret

    return inner


@log
def shoplist_add1():
    print('增加商品')


@log
def shoplist_del1():
    print('删除商品')


# shoplist_add1()

# 1.编写下载网页内容的函数，要求功能是：用户传入一个url，函数返回下载页面的结果
# 2.为题目1编写装饰器，实现缓存网页内容的功能：
# 具体：实现下载的页面存放于文件中，如果文件内有值（文件大小不为0），就优先从文件中读取网页内容，否则，就去下载，然后存到文件中


def cache(func):
    def inner(*args, **kwargs):
        if os.path.getsize('web_cache'):
            with open('web_cache', 'rb') as f:
                return f.read()
        ret = func(*args, **kwargs)
        with open('web_cache', 'wb') as f:
            # 写入的类型要一样,b转换一下类型
            f.write(b'*********' + ret)
        return ret

    return inner


@cache
def get(url):
    code = urlopen(url).read()
    return code


print(get('http://www.baidu.com'))
print(get('http://www.baidu.com'))
print(get('http://www.baidu.com'))
