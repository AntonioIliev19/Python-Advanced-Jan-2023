def find_element_in_matrix(matrix, element):
    for row_index in range(rows):
        for col_index in range(len(matrix[row_index])):
            if matrix[row_index][col_index] == element:
                return (row_index, col_index)


rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

symbol = input()
position = find_element_in_matrix(matrix, symbol)

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")


