from math import floor

size = int(input())

matrix = []
p_row = 0
p_col = 0
coins = 0

failed = False
won = False

for row in range(size):
    matrix.append([str(el) for el in input().split()])
    if 'P' in matrix[row]:
        p_row = row
        p_col = matrix[row].index('P')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

locations = []

while True:
    locations.append(f'[{p_row}, {p_col}]')
    direction = input()
    matrix[p_row][p_col] = '0'

    p_row += directions[direction][0]
    p_col += directions[direction][1]

    if p_row < 0:
        p_row = size - 1
    elif p_row == size:
        p_row = 0

    if p_col < 0:
        p_col = size - 1
    elif p_col == size:
        p_col = 0

    if matrix[p_row][p_col] == 'X':
        coins *= 0.5
        coins = floor(coins)
        failed = True
        locations.append(f'[{p_row}, {p_col}]')
        break
    coins += int(matrix[p_row][p_col])

    matrix[p_row][p_col] = 'P'
    if coins >= 100:
        won = True
        locations.append(f'[{p_row}, {p_col}]')
        break

if won:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")
print(f'Your path:')
for location in locations:
    print(location)
