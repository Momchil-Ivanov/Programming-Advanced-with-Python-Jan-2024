start_string = input()
size = int(input())
p_row = 0
p_col = 0
matrix = []

for row in range(size):
    matrix.append([str(el) for el in input()])
    if 'P' in matrix[row]:
        p_row = row
        p_col = matrix[row].index('P')

commands_count = int(input())

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for command in range(commands_count):
    direction = input()

    matrix[p_row][p_col] = '-'

    p_row += directions[direction][0]
    p_col += directions[direction][1]

    if not 0 <= p_row < size or not 0 <= p_col < size:
        if len(start_string) > 0:
            start_string = start_string[:-1]
        p_row -= directions[direction][0]
        p_col -= directions[direction][1]
        matrix[p_row][p_col] = 'P'
        continue

    if matrix[p_row][p_col] != '-':
        start_string += matrix[p_row][p_col]

    matrix[p_row][p_col] = 'P'

print(start_string)
for row in matrix:
    print("".join([str(el) for el in row]))
