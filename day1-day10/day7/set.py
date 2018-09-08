set1 = set({1, 2, 3, 3, 3, 3, 3})
set2 = {1.2, 1, 2, 3}
# print(set1, set2)

# 增加
set1.add('girl')
print(set1)
set1.update('text')
print(set1)

# 删除
print(set1.pop())
set1.remove(3)
print(set1)
set1.clear()
# del set1
print(set1)

# 查找
print('查找')
set3 = set({1, 2, 3})
for i in set3:
    print(i)

# 交集
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 3, 4, 5}
set3 = set1 & set2
print(set3)
print(set1.intersection(set2))

# 并集
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 3, 4, 5}
print(set1 | set2)
print(set1.union(set2))

# 反交集
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 3, 4, 5}
print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 差集
set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 3, 4, 5}
print(set1 - set2)
print(set1.difference(set2))

# 子集 超集
set1 = {4, 5}
set2 = {6, 7, 3, 4, 5}
print(set1 < set2)
print(set1.issubset(set2))

# 去重
li = [1, 2, 3, 5, 1, 2, 3, 6]
print(list(set(li)))

# 集合冻结
set1 = {1, 23}
set1 = frozenset(set1)
print(set1)
for i in set1:
    # 可以遍历
    print(i)
