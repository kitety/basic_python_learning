# str int
s = '2'
print(s.isspace())
'''
list:
'''
# 把数组的全部清空 用for循环
# 第一种 从后面往前面删除  第二种 照出来新建
li = [11, 22, 33, 44, 55]
for i in range(len(li) - 1, -1, -1):
    print(i, li)
    # 加上判断的话就删除奇数
    if i % 2 == 1:
        del li[i]
print(li)

# 删除带有'k'的键值对
dic = {'k1': 12, 'k2': 13, 'a1': 1}
dic1 = {}
# 换种思路
for i in dic:
    if 'k' not in i:
        dic1[i] = dic[i]
        # del dic[i]
        # 报错,循环的时候不能删除
dic = dic1
print(dic)

# 另外的思路 获取key 放入数组再循环删除
dic = {'k1': 12, 'k2': 13, 'a1': 1}
li = []
for i in dic:
    if 'k' in i:
        li.append(i)
for i in li:
    del dic[i]
print(dic)

# 元祖
tu = (1)
tu2 = (1, )
print(tu, type(tu))
# 只有一个元素,而且不加括号,那么就不会识别为元组长类型
print(tu2, type(tu2))
