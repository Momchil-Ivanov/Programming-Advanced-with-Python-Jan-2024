size = int(input())

j_row = 0
j_col = 0
matrix = []
enemies = 4
armor = 300

for row in range(size):
    matrix.append([str(el) for el in input()])
    if 'J' in matrix[row]:
        j_row = row
        j_col = matrix[row].index('J')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    direction = input()
    matrix[j_row][j_col] = '-'
    j_row += directions[direction][0]
    j_col += directions[direction][1]

    if matrix[j_row][j_col] == 'E':
        enemies -= 1
        if enemies == 0:
            print(f'Mission accomplished, you neutralized the aerial threat!')
            matrix[j_row][j_col] = 'J'
            break
        else:
            armor -= 100
            if armor == 0:
                print(f'Mission failed, your jetfighter was shot down! Last coordinates [{j_row}, {j_col}]!')
                matrix[j_row][j_col] = 'J'
                break
    elif matrix[j_row][j_col] == 'R':
        armor = 300


for row in matrix:
    print("".join([str(el) for el in row]))
