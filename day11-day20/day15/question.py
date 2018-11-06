def demo():
    # 定义生成器函数 0 1 2 3
    for i in range(4):
        yield i


g = demo()
# 生成器表达式
g1 = (i for i in g)
'''
def func():
    for i in g:
        yield i
'''
# 生成器要执行 g1--生成器没有执行
g2 = (i for i in g1)


# list 执行g1 只执行一次
# print(list(g1), type(g1))
# print(list(g2))


def add(n, i):
    return n + i


def test():
    for i in range(4):
        yield i


g = test()
# 数组1 10
for n in [1, 10]:
    g = (add(n, i) for i in g)
# 在list(g)的时候才执行
print(list(g))
'''
# 逐步替换
n=1
g=(add(1, i) for i in g)
n=10
g=(add(10, i) for i in g)
g=(add(10, i) for i in (add(10, i) for i in g))
g=(add(10, i) for i in (add(10, i) for i in (0,1,2,3)))
g=(add(10, i) for i in (10,11,12,13))
'''
