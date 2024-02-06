size = int(input())

matrix = []
ship_row = 0
ship_col = 0

fish_caught = 0
sank = False

for row in range(size):
    matrix.append([str(el) for el in input()])
    if 'S' in matrix[row]:
        col = matrix[row].index('S')
        ship_row = row
        ship_col = col

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    if command == 'collect the nets':
        break

    matrix[ship_row][ship_col] = '-'
    ship_row += directions[command][0]
    ship_col += directions[command][1]

    if ship_row < 0:
        ship_row = size - 1
    elif ship_row == size:
        ship_row = 0

    if ship_col < 0:
        ship_col = size - 1
    elif ship_col == size:
        ship_col = 0

    if matrix[ship_row][ship_col] == 'W':
        sank = True
        break
    elif matrix[ship_row][ship_col] != '-':
        fish_caught += int(matrix[ship_row][ship_col])

    matrix[ship_row][ship_col] = 'S'

if sank:
    print(f'You fell into a whirlpool! The ship sank and you lost the fish you caught. '
          f'Last coordinates of the ship: [{ship_row},{ship_col}]')
else:
    if fish_caught >= 20:
        print('Success! You managed to reach the quota!')
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! "
              f"You need {20 - fish_caught} tons of fish more.")

if fish_caught > 0 and not sank:
    print(f'Amount of fish caught: {fish_caught} tons.')
if not sank:
    for row in matrix:
        print(''.join(row))