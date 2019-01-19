# 读取文件函数
def get_line(filename):
    with open(filename, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            line_list = line.split(',')
            # 返回生成器
            yield line_list


# 过滤函数
def filter_user(condiction):
    '''条件筛选'''
    condiction = condiction.strip()
    if '>' in condiction:
        # 名目 阈值
        col, val = condiction.split('>')
        g = get_line('userinfo')
        for line in g:
            if int(line[dic[col]]) > int(val):
                print(line)
                yield line


def view(view, staff_g):
    '''展示符合条件的员工信息'''
    for staff_info in staff_g:
        

get_line('userinfo')

# 字典定义
dic = {
    'id': 0,
    'name': 1,
    'age': 2,
    'tel': 3,
    'job': 4
}

# ret=input('>>>')
ret = 'select name,age where age>0'
view, condiction = ret.split('where')
# view=view.split(' ')[1]
# print(view, condiction)
view = view.replace('select', ' ').strip()
view_list = view.split(',')
print(view_list, condiction)
filter_user(condiction)
