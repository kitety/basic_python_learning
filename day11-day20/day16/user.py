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
        # age 0
        col, val = condiction.split('>')
        g = get_line('userinfo')
        for line in g:
            if int(line[dic[col]]) > int(val):
                yield line
    if '<' in condiction:
        # 名目 阈值
        # age 0
        col, val = condiction.split('<')
        g = get_line('userinfo')
        for line in g:
            if int(line[dic[col]]) < int(val):
                yield line
    if '=' in condiction:
        # 名目 阈值
        # age 0
        col, val = condiction.split('=')
        g = get_line('userinfo')
        for line in g:
            if int(line[dic[col]]) == int(val):
                yield line

# 显示函数
def views(view, staff_g):
    '''展示符合条件的员工信息'''
    # 生成器 节省内存
    if '*' in view:
        view=dic.keys()
    for staff_info in staff_g:
        s = []
        for view_detail in view:
            s .append(staff_info[dic[view_detail]])
        print(s)



# 字典定义
dic = {
    'id': 0,
    'name': 1,
    'age': 2,
    'tel': 3,
    'job': 4
}

# ret=input('>>>')
# ret = 'select name,age where age>2'
ret = 'select * where age>2'
# 字段 条件
view, condiction = ret.split('where')
# 替换select
view = view.replace('select', ' ').strip()
# 转换为数组
view_list = view.split(',')
# 获取符合条件的元素 返回生成器
staff_g = filter_user(condiction)
# 展示数据
views(view_list, staff_g)
