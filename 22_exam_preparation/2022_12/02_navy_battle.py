size = int(input())

matrix = []
s_row = 0
s_col = 0

mine_hits = 0
cruisers_destroyed = 0

for row in range(size):
    matrix.append([str(el) for el in input()])
    if 'S' in matrix[row]:
        s_row = row
        s_col = matrix[row].index('S')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    command = input()
    matrix[s_row][s_col] = '-'

    s_row += directions[command][0]
    s_col += directions[command][1]
    if matrix[s_row][s_col] == '-':
        pass
    elif matrix[s_row][s_col] == '*':
        mine_hits += 1
        if mine_hits == 3:
            matrix[s_row][s_col] = 'S'
            print(f'Mission failed, U-9 disappeared! Last known coordinates [{s_row}, {s_col}]!')
            break
    elif matrix[s_row][s_col] == 'C':
        cruisers_destroyed += 1
        if cruisers_destroyed == 3:
            matrix[s_row][s_col] = 'S'
            print(f'Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
            break

for row in matrix:
    print("".join([str(el) for el in row]))
