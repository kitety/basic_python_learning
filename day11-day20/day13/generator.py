def generator1():
    print(1)
    print(1)
    yield 'a'


# yield
# 生成器函数 只用在函数中 不能和return一起用
# 生成器函数得到一个生成器作为返回值
ret = generator1()

# <generator object generator at 0x000001E45644EF68>
# print(ret)
# print('111')
# 1
# 1
# a
# print(ret.__next__())


def generator():
    print(1)
    yield 'a'
    print(1)
    yield 'b'


g = generator()
# ret=g.__next__()
# print(ret)
# ret=g.__next__()
# print(ret)

# for 循环 与上面的一样
for i in g:
    print(i)
'''
    yield 'wahaha'
    yield 'wahaha'
    yield 'wahaha'
    yield 'wahaha'
    yield 'wahaha'
在上面的语句中,并不是全部在内存中,只有当前的位置的在是在内存中的
'''


def wahaha():
    for i in range(2000000):
        yield 'wahaha%s' % i


#
g = wahaha()
count = 0
for i in g:
    count += 1
    print(i)
    if count > 50:
        break
count = 0
for i in g:
    count += 1
    print(i)
    if count > 50:
        break
