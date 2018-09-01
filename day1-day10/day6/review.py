# 1以66为边界分别准放入元组中
li = [11, 22, 33, 44, 55, 66, 77, 88, 99]
dic1 = {}
li_great = []
li_less = []
for i in li:
    if i < 66:
        li_less.append(i)
    else:
        li_great.append(i)
dic1.setdefault('k1', li_less)
dic1.setdefault('k2', li_great)
# print(dic1)
'''
输出商品列表，用户输入序号，显示用户选中的商品
    商品 li = ["手机", "电脑", '鼠标垫', '游艇']
要求:1：页面显示 序号 + 商品名称，如：
        1 手机
        2 电脑
    2： 用户输入选择的商品序号，然后打印商品名称
    3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
    4：用户输入'Q'或者'q'，退出程序。
'''
li = ["手机", "电脑", '鼠标垫', '游艇']
print('商品列表如下:')
for i in li:
    print('{}\t{}'.format(li.index(i) + 1, i))
while 1:
    number_choice = input('请输入序号,Q或者q退出:').strip()
    if number_choice.upper() == 'Q':
        print('已经退出')
        break
    elif number_choice.isdigit():
        number_choice = int(number_choice)
        if number_choice > 0 and number_choice <= len(li):
            print(li[number_choice - 1])
        else:
            print('请输入正确范围!')
    else:
        print('请输入数字')
