size = int(input())
number_of_bombs = int(input())

matrix = []
for _ in range(size):
    matrix.append([0] * size)

positions = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)

for _ in range(number_of_bombs):
    bomb_location = input()
    bomb_location = bomb_location[1:-1]
    bomb_list = bomb_location.split(', ')
    bomb_row = int(bomb_list[0])
    bomb_col = int(bomb_list[1])
    matrix[bomb_row][bomb_col] = '*'

    for pos in positions:
        current_row = bomb_row + pos[0]
        current_col = bomb_col + pos[1]
        if 0 <= current_row < size and 0 <= current_col < size and matrix[current_row][current_col] != '*':
            matrix[current_row][current_col] += 1
for row in matrix:
    print(' '.join(str(el) for el in row))