# 根据名，中间名，姓进行姓名存储
def init(data):
    """初始化"""
    data["first"] = {}
    data["middle"] = {}
    data["last"] = {}


def lookup(data, label, name):
    """根据指定的label和name来获取数据"""
    return data[label].get(name)


def store(data, full_name):
    """存储名字及其对应的结构"""
    names = full_name.split()
    if len(names) == 2:
        names.insert(1, "")
    labels = "first", "middle", "last"

    for label, name in zip(labels, names):
        people = lookup(data, label, name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]


def store2(data, *full_names):
    """
    多参数玩家名字存储

    :param data: 存储姓名的数据结构
    :param full_names: 输入的一系列玩家的名字
    :return: None
    """
    for full_name in full_names:
        store(data, full_name)


storage = {}
init(storage)
'''
store(storage, "Liu Wei")
store(storage, "Liu Yu Xin")
store(storage, "Liu De Hua")
'''
store2(storage, "Liu Wei", "Liu De Hua", "Liu Yu Xin")
v = lookup(storage, 'first', 'Liu')
print(v)

v = lookup(storage, 'last', 'Xin')
print(v)
