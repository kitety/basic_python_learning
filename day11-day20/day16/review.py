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
# print(format('test', '<20'))
# print(format('test', '>20'))
# print(format('test', '^20'))

# bytes转换成bytes类型
# bytes：unicode->utf8/gbk
# gbk->utf8:decode->Unicode->encode
# 两个的编码不同，需要转换
'''
bytes('你好', encoding='GBK')：Unicode的“你好”转成GBK编码，
bytes('你好', encoding='GBK').decode('GBK') 再decode成Unicode
bytes('你好', encoding='GBK').decode('GBK').encode('utf-8') 再编码为utf-8
'''
# print(bytes('你好', encoding='GBK').decode('GBK'))
# print(bytes('你好', encoding='GBK').decode('GBK').encode('utf-8'))
# print(bytes('你好', encoding='utf-8'))

# 网络编程 只能传二进制
# 照片和视频 二进制
# html网页爬虫也是bytes编码

# bytearray byte类型的数组
by_arr = bytearray('你好', encoding='utf-8')
# print(by_arr)
# 十六进制转换
# 长的字节可以指定位置替换，省内存空间
# print(by_arr[0])

# memoryview bytes类型转入memoryview之后就可以进行切片，不会创建新的，但是是字节类型的切片，不占内存，只是字节，转换为字符串会用空间
l = 'helloworld'
# print(l[:2]) # 占空间

# ord 字符按照unicode转数字
# print(ord('a'))
# print(ord('1'))

# chr 数字按照unicode转字符
# print(chr(97))

# ascii 是ascii的内容就打印，不是就转换为\u
# print(ascii('a'))
# print(ascii('好'))

# repr 用于r%格式化输出  可以包含引号
name = 'well'
print('你好%s' % name)
print('你好%r' % name)
print(repr(1))
print(repr('1'))
