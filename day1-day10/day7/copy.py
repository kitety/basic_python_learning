# import copy
# 赋值
# 相当于对应的是地址
li1 = [1, 2, 3]
l2 = li1
li1.append(12)
# 地址一样的
print(id(li1), id(l2))
# print(l2)

# copy 浅拷贝
l1 = [1, 2, 3, ['barry', 'alex']]

l2 = l1.copy()
print(l1, id(l1))  # [1, 2, 3, ['barry', 'alex']] 2380296895816
print(l2, id(l2))  # [1, 2, 3, ['barry'x, 'alex']] 2380296895048
l1[1] = 222
print(l1, id(l1))  # [1, 222, 3, ['barry', 'alex']] 2593038941128
print(l2, id(l2))  # [1, 2, 3, ['barry', 'alex']] 2593038941896

l1[3][0] = 'wusir'
print(l1, id(l1[3]))  # [1, 2, 3, ['wusir', 'alex']] 1732315659016
print(l2, id(l2[3]))  # [1, 2, 3, ['wusir', 'alex']] 1732315659016

# 深拷贝


l1 = [1, 2, 3, ['barry', 'alex']]
# l2 = copy.deepcopy(l1)
print(l1, id(l1))  # [1, 2, 3, ['barry', 'alex']] 2915377167816
print(l2, id(l2))  # [1, 2, 3, ['barry', 'alex']] 2915377167048
l1[1] = 222
print(l1, id(l1))  # [1, 222, 3, ['barry', 'alex']] 2915377167816
print(l2, id(l2))  # [1, 2, 3, ['barry', 'alex']] 2915377167048

l1[3][0] = 'wusir'
print(l1, id(l1[3]))  # [1, 222, 3, ['wusir', 'alex']] 2915377167240
print(l2, id(l2[3]))  # [1, 2, 3, ['barry', 'alex']] 2915377167304
