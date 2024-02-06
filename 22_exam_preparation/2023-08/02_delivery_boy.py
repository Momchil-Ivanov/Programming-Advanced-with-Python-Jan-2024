rows, cols = [int(el) for el in input().split()]

boy_row = 0
boy_col = 0
matrix =[]

for row in range(rows):
    matrix.append([str(el) for el in input()])
    if 'B' in matrix[row]:
        boy_row = row
        boy_col = matrix[row].index('B')

initial_row = boy_row
initial_col = boy_col

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

pizza = False
success = False

while True:
    command = input()
    boy_row += directions[command][0]
    boy_col += directions[command][1]

    if not (0 <= boy_row < rows and 0 <= boy_col < cols):
        matrix[initial_row][initial_col] = ' '
        break

    if matrix[boy_row][boy_col] == 'P':
        pizza = True
        print(f'Pizza is collected. 10 minutes for delivery.')
        matrix[boy_row][boy_col] = 'R'
    elif matrix[boy_row][boy_col] == '*':
        boy_row -= directions[command][0]
        boy_col -= directions[command][1]
    elif matrix[boy_row][boy_col] == 'A':
        if pizza:
            matrix[boy_row][boy_col] = 'P'
            matrix[initial_row][initial_col] = 'B'
            success = True
            break
    elif matrix[boy_row][boy_col] == '-':
        matrix[boy_row][boy_col] = '.'

if success:
    print(f'Pizza is delivered on time! Next order...')
else:
    print(f'The delivery is late. Order is canceled.')

for row in matrix:
    print(''.join(row))