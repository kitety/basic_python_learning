eggs_list = ['鸡蛋%s' % i for i in range(10)]
print(eggs_list)
list = []
for i in range(10):
    list.append('鸡蛋%s' % i)
print(list)
print([i for i in range(10)])

# 生成器表达式
g = (i for i in range(10))
for i in g:
    print(i)
