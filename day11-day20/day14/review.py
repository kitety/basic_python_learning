def generator():
    for i in range(20000):
        # 生成一条数据就返回一条数据
        yield '字符串_%s' % i


# 得到生成器
g = generator()
# 从生成器取值
# 方法1
# g.__next__()
# 方法2
num = 0
for i in g:
    num += 1
    if num > 50:
        break
    print(i)
# 方法3 占内存
li = list(g)
