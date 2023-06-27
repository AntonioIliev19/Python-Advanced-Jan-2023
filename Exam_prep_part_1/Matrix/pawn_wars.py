SIZE = 8

board = []
positions = [[], []]     # POSITIONS[0] ROW COL WHITE | POSITIONS[1] ROW COL BLACK


def save_positions(search_for, index_to_save, r):
    if search_for in board[r]:
        positions[index_to_save].append(r)
        positions[index_to_save].append(board[r].index(search_for))
        # ОТ РЕДА В КОЙТО Е НАМЕРЕН SEARCH_FOR(W OR B) ВЗИМАМЕ ИНДЕКСА И ГО АПЕНДВАМЕ В POS[0],[1]


for row in range(SIZE):     # 8 ROWS
    board.append(input().split())       # - - - - - - b - => [-, -, -, -, -, -, b, -]

    save_positions("w", 0, row)
    save_positions("b", 1, row)

if abs(positions[0][1] - positions[1][1]) != 1:
    if SIZE - positions[0][0] - 1 <= positions[1][0]:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + positions[1][1])}1.")
    else:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + positions[0][1])}8.")
else:
    place = (positions[0][0] + positions[1][0]) // 2

    if positions[0][0] % 2 == positions[1][0] % 2:
        print(f"Game over! Black win, capture on {chr(97 + positions[0][1])}{SIZE - place}.")
    else:
        print(f"Game over! White win, capture on {chr(97 + positions[1][1])}{SIZE - place}.")
