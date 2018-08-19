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
print(dic2)
