rows = int(input())
cols = rows

matrix = []

for row in range(0, rows):
    matrix.append([str(el) for el in input()])

element = str(input())

for row in range(0, rows):
    for col in range(0, cols):
        if matrix[row][col] == element:
            print(f"({row}, {col})")
            quit()

print(f"{element} does not occur in the matrix")