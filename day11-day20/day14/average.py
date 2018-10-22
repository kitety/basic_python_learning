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
ret = avg_g.send(112)
print(ret)
ret = avg_g.send(270)
print(ret)
ret = avg_g.send(300)
print(ret)

print('装饰器+生成器')


def init(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        # 先用next激活生成器
        g.__next__()
        return g

    return inner


# average1=init(average1)
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


avg_g = average1()
ret = avg_g.send(15)
print(ret)
ret = avg_g.send(30)
print(ret)


# python 3
# yield from
def generator2():
    a = '12345'
    b = 'abcde'
    # for i in a:
    #     yield i
    # for i in b:
    #     yield i
    #     新的
    yield from a
    yield from b


g = generator2()
for i in g:
    print(i)
