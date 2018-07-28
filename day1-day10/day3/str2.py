# 字符串的操作
# s = 'aleXWusir'
# 首字母大写
# print(s.capitalize())
# # 全大写
# print(s.upper())
# # 全小写
# print(s.lower())
# str1 = 'acER'
# yourStr = input('亲输入验证码:')
# if str1.upper() == yourStr.upper():
#     print('well')
# 大小写反转
# print(s.swapcase())
# s = 'alex weap'
# print(s.title())
# s = 'aleXW\tusir'
# 填充物居中填充
# print(s.center(50,'*'))
# print(s.expandtabs())
# 公共方法
# len长度
# s = '54645'
# print(len(s))
# 判断开头
# s = 'sdgshj'
# print(s.startswith('s'))
# print(s.startswith('g', 2))
# print(s.find('z'))
# # find()找不到返回-1 可以设置查找的始末 (友好)
# print(s.find('s'))
# # index()找不到报错 可以设置查找的始末
# print(s.index('sa'))
# s2 = '     nice well     '
# # strip() 去除空格 首尾
# print(s2.strip())
# # 迭代删除
# s3 = '**---**gggggg**'
# print(s3.strip('*-'))
# # lstrip() 删除左边 rstrip() 删除右边
# # count() 出现次数
# print(s3.count('g'))
# split() 拆分字符串 默认空格
# s = 'as df fg'
# print(s.split())
# s = 'as;df;fg'
# print(s.split(';'))
# format格式化
# s = '{}+{}+{}'.format(123, 456, 789)
# print(s)
# s = '{a}+{v}+{g}'.format(a=123, v=456, g=789)
# print(s)
# s = '{0}+{1}+{2}'.format(123, 456, 789)
# print(s)
# replace() 替换
# s = 'morning'
# # 替换 n为N 只替换一次,不加的话全部替换
# print(s.replace('n', 'N', 1))
# s = '123'
# print(s.isalnum()) #字母数字
# print(s.isalpha()) #字母
# print(s.isdigit()) # number
# for循环
# s = 'python'
# for i in s:
#     print(i, type(i))
s = 'good Morning'
if 'i' in s:
    print('i在字符串中')
