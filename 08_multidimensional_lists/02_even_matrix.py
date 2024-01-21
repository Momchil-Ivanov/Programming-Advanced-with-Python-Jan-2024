rows = int(input())

matrix = []

for row in range(0, rows):
    current_cols = [int(el) for el in input().split(', ') if int(el) % 2 == 0]
    matrix.append(current_cols)

print(matrix)