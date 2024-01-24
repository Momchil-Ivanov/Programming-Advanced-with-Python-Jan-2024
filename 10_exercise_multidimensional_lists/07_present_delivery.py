present_count = int(input())
size = int(input())

matrix = [[str(el) for el in input().split()] for row in range(size)]

nice_kids = 0
santa_row = 0
santa_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            santa_row = row
            santa_col = col

        if matrix[row][col] == "V":
            nice_kids += 1

nice_kids_total = nice_kids

while present_count > 0:
    command = input()
    if command == "Christmas morning":
        break

    matrix[santa_row][santa_col] = '-'

    if command == "up":
        santa_row -= 1
    elif command == "down":
        santa_row += 1
    elif command == "left":
        santa_col -= 1
    elif command == "right":
        santa_col += 1

    if matrix[santa_row][santa_col] == 'V':
        nice_kids -= 1
        present_count -= 1
    elif matrix[santa_row][santa_col] == 'C':
        matrix[santa_row][santa_col] = "S"
        # Left
        if matrix[santa_row][santa_col - 1] == "V" or matrix[santa_row][santa_col - 1] == "X":
            present_count -= 1
            if matrix[santa_row][santa_col - 1] == "V":
                nice_kids -= 1
            matrix[santa_row][santa_col - 1] = '-'
        if present_count == 0:
            break

        # Right
        if matrix[santa_row][santa_col + 1] == "V" or matrix[santa_row][santa_col + 1] == "X":
            present_count -= 1
            if matrix[santa_row][santa_col + 1] == "V":
                nice_kids -= 1
            matrix[santa_row][santa_col + 1] = '-'
        if present_count == 0:
            break

        # Up
        if matrix[santa_row - 1][santa_col] == "V" or matrix[santa_row - 1][santa_col] == "X":
            present_count -= 1
            if matrix[santa_row - 1][santa_col] == "V":
                nice_kids -= 1
            matrix[santa_row - 1][santa_col] = '-'
        if present_count == 0:
            break

        # Down
        if matrix[santa_row + 1][santa_col] == "V" or matrix[santa_row + 1][santa_col] == "X":
            present_count -= 1
            if matrix[santa_row + 1][santa_col] == "V":
                nice_kids -= 1
            matrix[santa_row + 1][santa_col] = '-'
        if present_count == 0:
            break
    matrix[santa_row][santa_col] = "S"

if present_count == 0 and nice_kids > 0:
    print('Santa ran out of presents!')

for row in matrix:
    print(*(row))

if nice_kids == 0:
    print(f"Good job, Santa! {nice_kids_total} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")