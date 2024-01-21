rows = int(input())

matrix = []

primary_diagonal_sum = 0

for row in range(0, rows):
    matrix.append([int(el) for el in input().split()])

for row in range(0, rows):
    col = row
    primary_diagonal_sum += matrix[row][col]

print(primary_diagonal_sum)