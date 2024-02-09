rows, cols = [int(el) for el in input().split()]

matrix = []
p_row = 0
p_col = 0

touched_people = 0
moves = 0

for row in range(rows):
    matrix.append([str(el) for el in input().split(' ')])
    if 'B' in matrix[row]:
        p_row = row
        p_col = matrix[row].index('B')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == 'Finish' or touched_people == 3:
        break

    ini_row = p_row
    ini_col = p_col
    p_row += directions[command][0]
    p_col += directions[command][1]

    if not 0 <= p_row < rows or not 0 <= p_col < cols or matrix[p_row][p_col] == 'O':
        p_row -= directions[command][0]
        p_col -= directions[command][1]
    else:
        matrix[ini_row][ini_col] = '-'
        if matrix[p_row][p_col] == 'P':
            touched_people += 1

        moves += 1
        matrix[p_row][p_col] = 'B'

print(f'Game over!')
print(f'Touched opponents: {touched_people} Moves made: {moves}')
