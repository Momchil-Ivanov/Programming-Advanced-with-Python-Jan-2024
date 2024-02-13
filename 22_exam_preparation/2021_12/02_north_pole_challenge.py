rows, cols = [int(el) for el in input().split(', ')]
y_row = 0
y_col = 0

matrix = []

decorations = 0
gifts = 0
cookies = 0

decorations_collected = 0
gifts_collected = 0
cookies_collected = 0

for row in range(rows):
    matrix.append([str(el) for el in input().split()])
    for col in range(cols):
        if matrix[row][col] == 'Y':
            y_row = row
            y_col = col
        elif matrix[row][col] == 'D':
            decorations += 1
        elif matrix[row][col] == 'G':
            gifts += 1
        elif matrix[row][col] == 'C':
            cookies += 1

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == 'End':
        break

    command_list = command.split('-')
    direction = command_list[0]
    moves = int(command_list[1])

    for move in range(moves):
        matrix[y_row][y_col] = 'x'

        y_row += directions[direction][0]
        y_col += directions[direction][1]

        if y_row < 0:
            y_row = rows - 1
        elif y_row == rows:
            y_row = 0

        if y_col < 0:
            y_col = cols - 1
        elif y_col == cols:
            y_col = 0

        if matrix[y_row][y_col] == 'D':
            decorations_collected += 1
            decorations -= 1
        elif matrix[y_row][y_col] == 'G':
            gifts_collected += 1
            gifts -= 1
        elif matrix[y_row][y_col] == 'C':
            cookies_collected += 1
            cookies -= 1

        matrix[y_row][y_col] = 'Y'

        if decorations == 0 and gifts == 0 and cookies == 0:
            print('Merry Christmas!')
            break
    if decorations == 0 and gifts == 0 and cookies == 0:
        break

print("You've collected:")
print(f'- {decorations_collected} Christmas decorations')
print(f'- {gifts_collected} Gifts')
print(f'- {cookies_collected} Cookies')

for row in matrix:
    print(' '.join([str(el) for el in row]))
