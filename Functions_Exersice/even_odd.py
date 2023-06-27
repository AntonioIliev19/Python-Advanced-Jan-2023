# def even_odd(*args):
#     command = args[-1]
#     even = []
#     odd = []
#     if command == "even":
#         for num in args[:-1]:
#             if num % 2 == 0:
#                 even.append(num)                                  Мое решение без компрехеншън
#         return even
#     elif command == "odd":
#         for num in args[:-1]:
#             if num % 2 != 0:
#                 odd.append(num)
#         return odd

def even_odd(*args):
    command = args[-1]

    if command == "even":
        return [a for a in args[:-1] if int(a) % 2 == 0]
    else:
        return [a for a in args[:-1] if int(a) % 2 != 0]


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))



