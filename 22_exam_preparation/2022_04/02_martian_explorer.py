size = 6

r_row = 0
r_col = 0
matrix = []

water_deposit = 0
metal_deposit = 0
concrete_deposit = 0

for row in range(size):
    matrix.append([str(el) for el in input().split()])
    if 'E' in matrix[row]:
        r_row = row
        r_col = matrix[row].index('E')

directions_list = input().split(', ')
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

broken = False
suitable = False

for direction in directions_list:
    matrix[r_row][r_col] = '-'

    r_row += directions[direction][0]
    r_col += directions[direction][1]

    if r_row < 0:
        r_row = size - 1
    elif r_row == size:
        r_row = 0

    if r_col < 0:
        r_col = size - 1
    elif r_col == size:
        r_col = 0

    if matrix[r_row][r_col] == 'W':
        water_deposit += 1
        print(f'Water deposit found at ({r_row}, {r_col})')
    elif matrix[r_row][r_col] == 'M':
        metal_deposit += 1
        print(f'Metal deposit found at ({r_row}, {r_col})')
    elif matrix[r_row][r_col] == 'C':
        print(f'Concrete deposit found at ({r_row}, {r_col})')
        concrete_deposit += 1
    elif matrix[r_row][r_col] == 'R':
        broken = True
        break

    if water_deposit == 1 and metal_deposit == 1 and concrete_deposit == 1:
        suitable = True

if broken:
    print(f'Rover got broken at ({r_row}, {r_col})')

if suitable:
    print(f'Area suitable to start the colony.')
else:
    print(f'Area not suitable to start the colony.')
