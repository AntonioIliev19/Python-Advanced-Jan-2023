def multiply(*args):
    res = 1
    for num in args:
        res *= num
    return res


print(multiply(2, 0, 1000, 5000))