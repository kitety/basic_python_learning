import time
time.time()

# time.sleep(5)


def func():
    print('大家好')


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
    def inner():
        start = time.time()
        # 被装饰函数
        f()
        time.sleep(0.5)
        end = time.time()
        print(end - start - 0.5)

    return inner


func = timer(func)
func()
