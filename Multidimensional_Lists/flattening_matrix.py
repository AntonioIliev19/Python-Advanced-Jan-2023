row = int(input())

flatten = []

for _ in range(row):
    num_in_column = [int(el) for el in input().split(", ")]
    flatten.extend(num_in_column)

print(flatten)