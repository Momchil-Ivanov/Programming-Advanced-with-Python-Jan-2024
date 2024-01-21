rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(0, rows):
    matrix.append([int(el) for el in input().split()])

for col in range(0, cols):
    current_col_sum = 0
    for row in range(0, rows):
        current_col_sum += matrix[row][col]
    print(current_col_sum)