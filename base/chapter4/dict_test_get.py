# 一个简单使用get的内存数据库

# 一个将人名作为键的字典。每个人都用一个字典表示，
# 字典包含键‘phone’和‘addr’,他们分别与电话号码和地址相关联
people = {
    'Alice': {
        'phone': '2314',
        'addr': 'Foo drive 23'
    },

    'Beth': {
        'phone': '9102',
        'addr': 'Bar street 42'
    },

    'Cecil': {
        'phone': '3158',
        'addr': 'Baz avenue 90'
    }
}

# 电话号码和地址的描述性标签，供打印输出时使用
labels = {
    'phone': 'phone number',
    'addr': 'address'
}

name = input('name:')

request = input('Phone number(p) or address(a)?')

key = ''
if request == 'p':
    key = 'phone'
if request == 'a':
    key = 'addr'

if name in people:
    print("{}'s {} is {}.".format(name, labels.get(key), people.get(name).get(key)))
