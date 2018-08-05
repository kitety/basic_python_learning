# li = ['alex', [1, 2, 3, 4, 5], 'beijing', '女神', 'taipei']
# print(li[0], li[1], li[2])
# print(li[:3])
# 列表的增删改查
li = ['alex', [1, 2, 3, 4, 5], 'beijing', '女神', 'taipei']
# li.append(45)
# print(li)
# 一个小例子
# li = []
# inpBool = True
# while inpBool:
#     inpVal = input('请输入一个值,输入q退出:')
#     if inpVal.lower().strip() == 'q':
#         inpBool = False
#     else:
#         li.append(inpVal)
# print('结束,当前列表为', li)

# 增
li = ['alex', [1, 2, 3, 4, 5], 'beijing', '女神', 'taipei']
li.insert(4, 'test')
li.extend('二哥')
li.extend([1, 2, 3])
# print(li)

# 删除
li = ['alex', [1, 2, 3, 4, 5], 'beijing', '女神', 'taipei']
# print(li.pop(), li)
# li.remove('alex')
# print(li)
# li.clear()
# print(li)
# del li
# print(li)
# 顾头不顾尾
# del li[2:]
# del li[:2]
# print(li)

# 改动
li = ['alex', [1, 2, 3, 4, 5], 'beijing', '女神', 'taipei']
# li[0] = [1, 2, 3]
# li[0:2] = [1, 2, 3, '12345']
# print(li)

# 查
li = ['alex', [1, 2, 3, 4, 5], 'beijing', '女神', 'taipei']
# for i in li[:2]:
#     print(type(i))

# 公共方法
# print(len(li))
# print(li.count('女神1'))
# print(li.index('女神'))

# 排序
li = [1, 5, 8, 7, 4, 6]
# li.sort(reverse=True)
li.reverse()
print(li)
