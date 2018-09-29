# 装饰器
# 原则:开放封闭原则
# 作用:不改变原来的函数调用方式,在函数前后添加新功能
# 本质:闭包函数


def wrapper(func):
    def inner(*args, **kwargs):
        print('执行之前做的事情')
        ret = func(*args, **kwargs)
        print('执行之前做的事情')
        return ret

    return inner


@wrapper
def holiday(day):
    print('放假%s天' % day)
    return 'happy'


print(holiday(12))
