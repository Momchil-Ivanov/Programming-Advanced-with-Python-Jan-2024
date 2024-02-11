size = 6

matrix = []

for row in range(size):
    matrix.append([el for el in input().split(' ')])

coordinates = input().split(', ')
p_row = int(coordinates[0].replace('(',''))
p_col = int(coordinates[1].replace(')',''))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == "Stop":
        break

    command_to_list = command.split(', ')
    action = command_to_list[0]
    direction = command_to_list[1]

    p_row += directions[direction][0]
    p_col += directions[direction][1]

    if action == 'Create':
        value = command_to_list[2]
        if matrix[p_row][p_col] == '.':
            matrix[p_row][p_col] = value
    elif action == 'Update':
        value = command_to_list[2]
        if not matrix[p_row][p_col] == '.':
            matrix[p_row][p_col] = value
    elif action == 'Delete':
        if not matrix[p_row][p_col] == '.':
            matrix[p_row][p_col] = '.'
    elif action == 'Read':
        if not matrix[p_row][p_col] == '.':
            print(matrix[p_row][p_col])

for row in matrix:
    print(" ".join(row))
