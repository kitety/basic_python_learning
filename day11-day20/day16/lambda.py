# calc=lambda n:n**n
def calc(n): return n**n


print(calc(4))

# add=lambda x,y: x+y


def add(x, y): return x+y


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


def d(p): return p*2


def t(p): return p*3


x = 2
x = d(x)
x = t(x)
x = d(x)
# print(x)

print('   元组转换')
# 两个元组，((('a'),('b')),(('c'),('d'))),用匿名函数生成列表[{'a','c'},{'b','d'}]
# zip 返回一个迭代器
# 匿名函数，内置函数
ret = zip(((('a'), ('b')), (('c'), ('d'))))
print(ret)
for ii in ret:
    print(ii)


def func(tuple):
    return {tuple[0]: tuple[1]}


res = map(func, ret)
print(list(res))
