# 递归示例
def factorial(n):
    """阶乘"""
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)


print(factorial(3))
print(factorial(4))
print(factorial(100))
