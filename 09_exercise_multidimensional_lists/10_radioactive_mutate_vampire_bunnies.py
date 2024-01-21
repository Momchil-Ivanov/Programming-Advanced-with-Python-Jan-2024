import copy

rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(0, rows):
    matrix.append([str(el) for el in input()])

matrix_ini = copy.deepcopy(matrix)

directions = [str(el) for el in input()]

player_row = 0
player_col = 0
player_found = False
won = False

for row in range(0, rows):
    for col in range(0, cols):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col
            player_found = True
            break
    if player_found:
        break

won = False
alive = True

for direction in directions:
    if won or not alive:
        break
    matrix[player_row][player_col] = "."

    if direction == "L":
        if player_col - 1 < 0:
            won = True
        else:
            player_col -= 1
    elif direction == "R":
        if player_col + 1 == cols:
            won = True
        else:
            player_col += 1
    elif direction == "U":
        if player_row - 1 < 0:
            won = True
        else:
            player_row -= 1
    elif direction == "D":
        if player_row + 1 == rows:
            won = True
        else:
            player_row += 1

    if matrix[player_row][player_col] == "B":
        alive = False
    elif not won:
        matrix[player_row][player_col] = "P"

    matrix_ini = copy.deepcopy(matrix)

    for row in range(0, rows):
        for col in range(0, cols):
            if matrix_ini[row][col] == "B":
                if row - 1 >= 0:
                    matrix[row - 1][col] = "B"
                if row + 1 < rows:
                    matrix[row + 1][col] = "B"
                if col - 1 >= 0:
                    matrix[row][col - 1] = "B"
                if col + 1 < cols:
                    matrix[row][col + 1] = "B"

    player_still_alive = False

    for row in range(0, rows):
        for col in range(0, cols):
            if matrix[row][col] == "P":
                player_still_alive = True

    if not player_still_alive and not won:
        alive = False

for row in matrix:
    print(''.join(str(el) for el in row))

if alive:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")