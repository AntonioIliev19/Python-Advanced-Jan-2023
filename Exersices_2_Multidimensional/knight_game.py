size = int(input())
matrix = [list(input()) for _ in range(size)]
positions = (
    (-2, -1),  # up 2 left 1
    (-2, 1),  # up 2 right 1
    (-1, -2),  # up 1 left 2
    (-1, 2),  # up 1 right 2
    (2, 1),  # down 2 right 1
    (2, -1),  # down 2 left 1
    (1, 2),  # down 1 right 2
    (1, -2),  # down 1 left 2
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_att_pos = []

    for rows in range(size):
        for cols in range(size):
            if matrix[rows][cols] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = rows + pos[0]
                    pos_col = cols + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_att_pos = [rows, cols]
                    max_attacks = attacks

    if knight_with_most_att_pos:
        matrix[knight_with_most_att_pos[0]][knight_with_most_att_pos[1]] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)