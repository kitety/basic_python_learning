def generator():
    print(123)
    yield 2
    print(456)
    yield 3
    print(789)


# 有几个yield就返回几个值

g = generator()

# 得到生成器
# for i in g:
#     print(i, '生成器的生成')

# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)
# # 读出789,报错
# ret = g.__next__()
# # ret = g.send(None)
# print(ret)


def generator1():
    print(123)
    content = yield 2
    print('```', content)
    print(456)
    yield 3
    yield 4


g1 = generator1()
ret = g1.send(None)
# ret = g1.__next__()
print(ret)
# 以上 打印 123   2
ret = g1.send('send_data')
print(ret)
# 以上打印 ``` send_data 456 3
ret = g1.send(None)
print(ret)
# 打印4

# 或者在最后yield空,这种情况是在(yield 参数)之后还有我需要的代码执行,通过这种方式可以满足要求
