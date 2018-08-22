dict1 = {
    'name': ['alex', 'cool'],
    'py9': [{
        'name': 'test',
        'ave_age': 18
    }],
    True: 1
}
# print(dict1)
dic = {'name': 'text_name', 'age': 18, 'sex': 'man'}
# 增
dic['height'] = 185  # 没有就添加,有就修改
dic['age'] = 14
dic.setdefault('grade', 3)
# 删
dic.pop('name', None)
dic.popitem()
# dic.clear() # 清空
# del dic['name']
# print(dic)
# 改
dic['height'] = 185  # 没有就添加,有就修改
dic1 = {'name': 'text_name2', 'age': 182, 'sex': 'man2'}
dic2 = {'name': 'text_name', 'age': 18, 'sex': 'man', 'test': True}
dic2.update(dic1)
# print(dic2)

# 查
dic1 = {'name': 'text_name2', 'age': 182, 'sex': 'man2'}
# print(dic1.keys(), type(dic1.keys()))
# print(dic1.values())
# print(dic1.items())
# for i in dic1:
#     print(i)
# for i in dic1.values():
#     print(i)
for k, v in dic1.items():
    print(k, v)

# 分别赋值
a, b = 1, 2
a, b = b, a
# print(a, b)
a, b = [1, 2]
a, b = (1, 2)
a, b = [1, 2], [3, 4]
# print(a, b)
# 指定打印某一项
print(dic1['name'])
print(dic1.get('cool12', 'nothisvalue'))
