# 关键字参数
def hello(greeting="hello", name="world"):
    print('{} {}'.format(greeting, name))


hello("hello", "vv1")
hello(greeting="hello", name="vv2")
hello()
