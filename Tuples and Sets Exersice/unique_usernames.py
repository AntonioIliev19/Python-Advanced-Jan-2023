# n = int(input())
# names = set()
#
#
# for _ in range(n):
#     name = input()
#     names.add(name)
#
# for name in names:
#     print(name)


n = int(input())
names = set()

for _ in range(n):
    names.add(input())

print(*names, sep="\n")

print(*{input() for _ in range(int(input()))}, sep="\n")

