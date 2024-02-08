hazelnuts = 0

size = int(input())

matrix = []

s_row = 0
s_col = 0

commands = input().split(', ')

for row in range(size):
    matrix.append([str(el) for el in input()])
    if 's' in matrix[row]:
        s_row = row
        s_col = matrix[row].index('s')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'right': (0, 1),
    'left': (0, -1)
}

ended = False

for command in commands:
    matrix[s_row][s_col] = '*'

    s_row += directions[command][0]
    s_col += directions[command][1]

    if not 0 <= s_row < size or not 0 <= s_col < size:
        print(f'The squirrel is out of the field.')
        ended = True
        break

    if matrix[s_row][s_col] == 'h':
        hazelnuts += 1
        if hazelnuts == 3:
            print(f'Good job! You have collected all hazelnuts!')
            ended = True
            break
    elif matrix[s_row][s_col] == 't':
        print(f'Unfortunately, the squirrel stepped on a trap...')
        ended = True
        break

if hazelnuts < 3 and not ended:
    print(f'There are more hazelnuts to collect.')

print(f'Hazelnuts collected: {hazelnuts}')
