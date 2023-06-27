rows = int(input())

matrix = []


for _ in range(rows):
    num_in_column = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(num_in_column)

print(matrix)