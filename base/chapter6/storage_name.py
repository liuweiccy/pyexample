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


storage = {}
init(storage)
store(storage, "Liu Wei")
store(storage, "Liu Yu Xin")
store(storage, "Liu De Hua")
v = lookup(storage, 'first', 'Liu')
print(v)

v = lookup(storage, 'last', 'Xin')
print(v)
