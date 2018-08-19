lis = [2, 3, 'k', ['qwe', 20, ['k', ['tt', 3, '1']], 89], 'ab', 'adv']
# 第一,'tt'=>'TT'
# lis[3][2][1][0] = lis[3][2][1][0].upper()
lis[3][2][1][0] = 'TT'
# 第二 列表的1=>'100'
lis[1] = '100'
# 2)将列表中的数字3变成字符串’100’（用两种方式）。
lis[3][2][1].remove(3)
lis[3][2][1].insert(1, '100')
# print(lis)

# 查找列表li中的元素，移除每个元素的空格，并找出以’A’或者’a’开头，并以’c’结尾的所有元素，并添加到一个新列表中,最后循环打印这个新列表。
li = ['taibai ', 'alexC', 'AbC ', 'egon', ' Ritian', ' Wusir', '  aqc']
b = []
for i in li:
    s = i.strip()
    if (s.startswith('a') or s.startswith('A')) and s.endswith('c'):
        b.append(s)
for i in b:
    print(i)

# li1 = ['张三', '李四']敏感词过滤,从输入中过滤
li1 = ['张三', '李四']
new_li1 = []
info = input('请输入内容:').strip()
for i in li1:
    if i in info:
        info = info.replace(i, '*' * len(i))
new_li1.append(info)
print(new_li1)
