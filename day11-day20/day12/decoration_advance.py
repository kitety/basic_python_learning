import time

flag = False


def timer_out(flag):
    def timmer(func):
        def inner(*args, **kwargs):
            if flag:
                start = time.time()
                ret = func(*args, **kwargs)
                end = time.time()
                print(end - start)
                return ret
            else:
                ret = func(*args, **kwargs)
                return ret

        return inner

    return timmer


# 加括号就是调用,返回timer
@timer_out(flag)
def wahaha():
    print('wahaha')


@timer_out(flag)
def wine():
    print('wine')


# wahaha()
# wine()


def wrapper1(func):
    def inner1(*args, **kwargs):
        print(1)
        ret = func(*args, **kwargs)
        print(11)
        return ret

    return inner1


def wrapper2(func):
    def inner2(*args, **kwargs):
        print(2)
        ret = func(*args, **kwargs)
        print(22)
        return ret

    return inner2


# 把下面的都当成func
@wrapper1  # f=inner1cccc
@wrapper2  # f=inner2
def main():
    print('main')


main()
