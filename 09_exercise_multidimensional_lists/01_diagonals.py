rows = int(input())
cols = rows

matrix = []

primary_diagonal_sum = 0
secondary_diagonal_sum = 0
primary_diagonals = []
secondary_diagonals = []

for row in range(0, rows):
    matrix.append([int(el) for el in input().split(', ')])

for row in range(0, rows):
    primary_diagonal_value = matrix[row][row]
    primary_diagonals.append(primary_diagonal_value)
    primary_diagonal_sum += primary_diagonal_value

    secondary_diagonal_value = matrix[row][rows - 1 - row]
    secondary_diagonals.append(secondary_diagonal_value)
    secondary_diagonal_sum += secondary_diagonal_value

print(f"Primary diagonal: {', '.join([str(el) for el in primary_diagonals])}. \
Sum: {primary_diagonal_sum}")

print(f"Secondary diagonal: {', '.join([str(el) for el in secondary_diagonals])}. \
Sum: {secondary_diagonal_sum}")