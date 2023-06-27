rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

max_sum = float('-inf')
sub_matrix = []

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current_el = matrix[row_index][col_index]
        element_below = matrix[row_index + 1][col_index]
        next_element = matrix[row_index][col_index + 1]
        diagonal_el = matrix[row_index + 1][col_index + 1]
        sum_el = current_el + element_below + next_element + diagonal_el

        if max_sum < sum_el:
            max_sum = sum_el
            sub_matrix = [[current_el, next_element], [element_below, diagonal_el]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
