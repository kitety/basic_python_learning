# 处理文件,用户指定要查找的文件的内容,讲文件中包含要查找的一行都输出到屏幕
def check_file(filename, aim):
    with open(filename, encoding="utf-8") as f:
        # f文件句柄 文件操作符 handler
        for i in f:
            if (aim in i):
                yield i


g = check_file('text.txt', '山')

# for i in g:
#     print(i.strip())


# 写生成器,在文件中读取内容,在每一次读取到的内容前加上'***'后返回给用户
def check_add(filename):
    with open(filename, encoding="utf-8") as f:
        # f文件句柄 文件操作符 handler
        for i in f:
            yield '***' + i


g = check_add('text.txt')
for i in g:
    print(i.strip())
