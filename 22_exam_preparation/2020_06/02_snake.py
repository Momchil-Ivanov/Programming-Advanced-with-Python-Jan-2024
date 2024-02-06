size = int(input())
matrix = [[str(el) for el in input()] for _ in range(size)]

snake_found = False

snake_col = 0
snake_row = 0
food = 0
won = False

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'S':
            snake_row = row
            snake_col = col
            snake_found = True
            break
    if snake_found:
        break

while True:
    command = input()
    matrix[snake_row][snake_col] = '.'
    if command == 'left':
        if snake_col - 1 < 0:
            break
        else:
            if matrix[snake_row][snake_col - 1] == '*':
                food += 1
                snake_col -= 1
            elif matrix[snake_row][snake_col - 1] == 'B':
                matrix[snake_row][snake_col - 1] = '.'
                for row in range(size):
                    for col in range(size):
                        if matrix[row][col] == 'B':
                            snake_row = row
                            snake_col = col
                            break
            else:
                snake_col -= 1
    elif command == 'right':
        if snake_col + 1 == size:
            break
        else:
            if matrix[snake_row][snake_col + 1] == '*':
                food += 1
                snake_col += 1
            elif matrix[snake_row][snake_col + 1] == 'B':
                matrix[snake_row][snake_col + 1] = '.'
                for row in range(size):
                    for col in range(size):
                        if matrix[row][col] == 'B':
                            snake_row = row
                            snake_col = col
                            break
            else:
                snake_col += 1
    elif command == 'up':
        if snake_row - 1 < 0:
            break
        else:
            if matrix[snake_row - 1][snake_col] == '*':
                food += 1
                snake_row -= 1
            elif matrix[snake_row - 1][snake_col] == 'B':
                matrix[snake_row - 1][snake_col] = '.'
                for row in range(size):
                    for col in range(size):
                        if matrix[row][col] == 'B':
                            snake_row = row
                            snake_col = col
                            break
            else:
                snake_row -= 1
    elif command == 'down':
        if snake_row + 1 == size:
            break
        else:
            if matrix[snake_row + 1][snake_col] == '*':
                food += 1
                snake_row += 1
            elif matrix[snake_row + 1][snake_col] == 'B':
                matrix[snake_row + 1][snake_col] = '.'
                for row in range(size):
                    for col in range(size):
                        if matrix[row][col] == 'B':
                            snake_row = row
                            snake_col = col
                            break
            else:
                snake_row += 1

    matrix[snake_row][snake_col] = 'S'
    if food == 10:
        won = True
        break

if won:
    print(f'You won! You fed the snake.')
else:
    print(f'Game over!')
print(f'Food eaten: {food}')

for row in matrix:
    print(''.join(str(el) for el in row))