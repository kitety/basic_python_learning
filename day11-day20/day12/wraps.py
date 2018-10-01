from functools import wraps


def wahaha():
    '''
    1212
    '''
    print(21)


print(wahaha.__name__)
print(wahaha.__doc__)


def wrapper(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print('执行之前做的事情')
        ret = func(*args, **kwargs)
        print('执行之前做的事情')
        return ret

    return inner


@wrapper
def holiday(day):
    '''
    12122 注释
    '''
    print('放假%s天' % day)
    return 'happy'


print(holiday.__name__)
print(holiday.__doc__)
