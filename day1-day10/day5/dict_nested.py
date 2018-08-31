dic = {
    'name': ['alex', 'wusir', 'taibai'],
    'py9': {
        'time': '1213',
        'learn_money': 19800,
        'address': 'CBD'
    },
    'age': 21
}
# 修改年龄
dic['age'] = 22
# name list添加元素
dic['name'].append('addTest')
# name list的wusir大写
dic['name'][1] = dic['name'][1].upper()
# py9里面添加键值对
dic['py9']['number'] = 6
# print(dic)

# 检测输入的字符串的数字
info = input('请输入:').strip()
# 这里的info是不可变的,已经读到了内存
for i in info:
    if i.isalpha():
        # 循环的时候也可以用
        info = info.replace(i, ' ')
print(info.split())

