def generator():
    print(123)
    yield 2
    print(456)
    yield 3
    print(789)


g = generator()


# 得到生成器
# for i in g:
#     print(i, 122)

# ret = g.__next__()
# print(ret)
# ret = g.__next__()
# print(ret)
# # 读出789,报错
# ret = g.__next__()
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
ret = g1.send('send_data')
print(ret)
ret = g1.send(None)
print(ret)
