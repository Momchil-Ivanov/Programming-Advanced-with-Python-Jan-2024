w_row = 0
w_col = 0
b_row = 0
b_col = 0

matrix = []

size = 8

for row in range(size):
    matrix.append([str(el) for el in input().split(' ')])
    if 'w' in matrix[row]:
        w_row = row
        w_col = matrix[row].index('w')
    if 'b' in matrix[row]:
        b_row = row
        b_col = matrix[row].index('b')

queen = False
white_win = False
black_win = False

while True:

    if w_col - 1 >= 0:
        if matrix[w_row - 1][w_col - 1] == 'b':
            w_row -= 1
            w_col -= 1
            white_win = True
            break
    if w_col + 1 < size:
        if matrix[w_row - 1][w_col + 1] == 'b':
            w_row -= 1
            w_col += 1
            white_win = True
            break

    matrix[w_row][w_col] = '-'
    w_row -= 1
    matrix[w_row][w_col] = 'w'
    if w_row == 0:
        queen = True
        white_win = True
        break

    if b_col - 1 >= 0:
        if matrix[b_row + 1][b_col - 1] == 'w':
            b_row += 1
            b_col -= 1
            black_win = True
            break
    if b_col + 1 < size:
        if matrix[b_row + 1][b_col + 1] == 'w':
            b_row += 1
            b_col += 1
            black_win = True
            break

    matrix[b_row][b_col] = '-'
    b_row += 1
    matrix[b_row][b_col] = 'b'
    if b_row == 7:
        queen = True
        black_win = True
        break

if white_win:
    w_row_to_number = 8 - w_row
    w_col_to_letter = chr(97 + w_col)
    if queen:
        print(f'Game over! White pawn is promoted to a queen at {w_col_to_letter}{w_row_to_number}.')
    else:
        print(f'Game over! White win, capture on {w_col_to_letter}{w_row_to_number}.')
else:
    b_row_to_number = 8 - b_row
    b_col_to_letter = chr(97 + b_col)
    if queen:
        print(f'Game over! Black pawn is promoted to a queen at {b_col_to_letter}{b_row_to_number}.')
    else:
        print(f'Game over! Black win, capture on {b_col_to_letter}{b_row_to_number}.')
