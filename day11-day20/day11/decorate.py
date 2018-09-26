import time
time.time()

# time.sleep(5)


# 函数的计算时间计算函数
def f_timer(f):
    start = time.time()
    f()
    time.sleep(0.5)
    end = time.time()
    print(end - start - 0.5)


# f_timer(func)
# 新的函数  装饰器函数
def timer(f):
    # 闭包:函数嵌套+使用外部变量
    def inner(*args, **kwargs):
        start = time.time()
        # 被装饰函数
        r = f(*args, **kwargs)
        time.sleep(0.5)
        end = time.time()
        print(end - start - 0.5, 121212)
        return r

    return inner


# 这个是语法糖
# 上面的是装饰器函数名  下面的是被装饰的函数
@timer
def func(a, b):
    print('大家好', a, b)
    return 'hello everyone'


# 被语法糖替换了 其实是inner
# func = timer(func)
ret = func(1, b=2)
print(ret)

# 装饰器 有返回值 有参数 万能参数


# 真实的样子
# f 被装饰的函数
def wrapper(f):
    def inner(*args, **kwargs):
        # 被装饰函数之前的执行
        r = f(*args, **kwargs)  # 被装饰的函数
        # 被装饰函数之后的执行
        return r

    return inner


@wrapper
def func1(a, b):
    print('大家好', a, b)
    return 'hello everyone'
