# 检查用户名和pin码

database = [
    ['vv', 1234],
    ['yy', 45765],
    ['xx', 8723]
]

name = input("name:")
pin = int(input("pin code:"))

if [name, pin] in database:
    print("Access granted")
