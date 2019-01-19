# calc=lambda n:n**n
def calc(n): return n ** n


print(calc(4))


# add=lambda x,y: x+y


def add(x, y): return x + y


# 取出字典的最大值
dic = {'k1': 1, 'k2': 222, 'k3': 99}


def fun(key):
    return dic[key]


print(dic[max(dic, key=fun)])
# 转为匿名函数


dic = {'k1': 1, 'k2': 222, 'k3': 99}
print(max(dic))
print(dic[max(dic, key=lambda k: dic[k])])
# 默认max排序是针对的是字典里面的key

print('    匿名函数在filter')
# 匿名函数在filter
res = filter(lambda x: x > 10, [5, 8, 12, 14, 15, 16])
for i in res:
    print(i)


# max min filter map sorted 都有可以跟key=>lambda


def d(p): return p * 2


def t(p): return p * 3


x = 2
x = d(x)
x = t(x)
x = d(x)
# print(x)

print('   元组转换')
# 两个元组，((('a'),('b')),(('c'),('d'))),用匿名函数生成列表[{'a','c'},{'b','d'}]
# zip 返回一个迭代器
# 匿名函数，内置函数
ret = zip((('a'), ('b')), (('c'), ('d')))


def func(tuple):
    return {tuple[0]: tuple[1]}


# res = map(func, ret)
# print(list(res))
res = map(lambda x: {x[0]: x[1]}, ret)
print(list(res))


def multipliers():
    # 返回list
    return [lambda x: i * x for i in range(4)]


# 返回匿名函数
# 执行的时候是最后,for循环已经执行完毕,是3(最后一个i)
print([m(2) for m in multipliers()])


def multipliers():
    # 生成器表达式
    return (lambda x: i * x for i in range(4))


# 返回匿名函数
# 执行的时候是最后,for循环已经执行完毕,是3(最后一个i)
print([m(2) for m in multipliers()])
