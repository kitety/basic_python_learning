'''
数据类型：int bool tuple dict str
数据结构（容器）： list dict tuple set str
'''
# reversed()
list1 = [1, 2, 3]
list1.reverse()
# 不改变原来的，返回迭代器
list2 = reversed(list1)
# print(list1)
# print(list2)

# slice 切片
l1 = [1, 2, 3, 4, 5, 6]
sli = slice(1, 5, 2)
# print(sli, l1[sli])
# print(l1[1:5:2])

# format() 保留小数，浮点数，进制转换
# 格式调整 左对齐，右对齐，居中
print(format('test', '<20'))
print(format('test', '>20'))
print(format('test', '^20'))

# bytes转换成bytes类型
# bytes：unicode->utf8/gbk
# gbk->utf8:decode->encode
# 两个的编码不同
print(bytes('你好', encoding='GBK').decode('GBK'))
print(bytes('你好', encoding='utf-8'))
