# def average():
#     sum_all = 0
#     count = 0
#     avg = 0
#     num = yield
#     sum_all += num
#     count += 1
#     avg = sum_all / count
#     yield avg


# 移动平均值
def average():
    sum_all = 0
    count = 0
    avg = 0
    while 1:
        num = yield avg
        sum_all += num
        count += 1
        avg = sum_all / count


avg_g = average()
# 到达yield
avg_g.send(None)
# ret = avg_g.send(10)
# print(ret)
# ret = avg_g.send(20)
# print(ret)
# ret = avg_g.send(30)
# print(ret)

print('装饰器+生成器')


def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        # 先用next激活生成器
        g.__next__()
        return g

    return inner


@init
def average1():
    sum_all = 0
    count = 0
    avg = 0
    while 1:
        num = yield avg
        sum_all += num
        count += 1
        avg = sum_all / count


ret = avg_g.send(15)
print(ret)
ret = avg_g.send(30)
print(ret)
