# 查找 找数据
# 最短路径
l = [2, 3, 5, 10, 15, 16, 18, 22, 26, 30, 32, 35, 41, 42, 43, 55, 56, 66, 67, 69, 72, 76, 82, 83, 88]


# 查找 有问题
# def find(l, aim_num):
#     mid_index = len(l) // 2
#     if l[mid_index] < aim_num:
#         find(l[mid_index + 1:], aim_num)
#     elif l[mid_index] > aim_num:
#         find(l[:mid_index], aim_num)
#     else:
#         print( l[mid_index])
#
#
# find(l, 66)

# 上面的那个出现索引值有问题

def find(l, aim_number, start=0, end=None):
    # 判断一下end
    end = len(l) if end is None else end
    mid_index = start + (end - start) // 2
    # 注意start,end的变化
    if start < end:
        if l[mid_index] < aim_number:
            return find(l, aim_number, start=mid_index + 1, end=len(l))
        elif l[mid_index] > aim_number:
            return find(l, aim_number, start=start, end=mid_index - 1)
        else:
            return mid_index
    else:
        return None


print(find(l, 66))

# 参数  返回值 找不到
