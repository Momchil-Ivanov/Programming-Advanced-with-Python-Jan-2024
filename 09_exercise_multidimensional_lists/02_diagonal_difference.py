rows = int(input())
cols = rows

matrix = []

primary_diagonal_sum = 0
secondary_diagonal_sum = 0

for row in range(0, rows):
    matrix.append([int(el) for el in input().split(' ')])

for row in range(0, rows):
    primary_diagonal_value = matrix[row][row]
    primary_diagonal_sum += primary_diagonal_value

    secondary_diagonal_value = matrix[row][rows - 1 - row]
    secondary_diagonal_sum += secondary_diagonal_value

difference = abs(primary_diagonal_sum - secondary_diagonal_sum)
print(difference)