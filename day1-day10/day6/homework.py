li = [{
    'name': '苹果',
    'price': 18
}, {
    'name': '香蕉',
    'price': 15
}, {
    'name': '西瓜',
    'price': 12
}]
shop_car = {}
print('欢迎光临水果店!!')
money = input('让我看看你的钱:')
if str(money).isdigit() and int(money) > 0:
    while 1:
        for i, k in enumerate(li):
            print('序号:{},商品:{},价格:{}'.format(i + 1, k['name'], k['price']))
        choose = input('请输入您要购买的序号:')
        if choose.isdigit() and int(choose) <= len(li) and int(choose) > 0:
            number = input('请输入您要购买的数量:')
            if number.isdigit():
                money = int(money) - li[int(choose) - 1]['price'] * int(number)
                if money >= 0:
                    if li[int(choose) - 1]['name'] in shop_car:
                        shop_car[li[int(choose) - 1][
                            'name']] = shop_car[li[int(choose) -
                                                   1]['name']] + int(number)
                    else:
                        shop_car[li[int(choose) - 1]['name']] = int(number)
                    print('购物车的商品有{},您还有{}元钱'.format(shop_car, money))
                else:
                    print('购买失败,钱不够')
                    break
        else:
            print('请输入序号!')
