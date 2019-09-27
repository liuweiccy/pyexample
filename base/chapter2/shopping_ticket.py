# 根据指定的宽度打印格式良好的购物小票
width = int(input('Please enter width:'))

price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('=' * width)
print(header_fmt.format("Item", "Price"))
print('-' * width)
print(fmt.format("Apple", 0.4))
print(fmt.format("Pear", 0.5))
print(fmt.format("Apple Phone", 999))
print(fmt.format("Beer (4L)", 40))
print(fmt.format("Meat (5kg * 2)", 29.99))
print('=' * width)
