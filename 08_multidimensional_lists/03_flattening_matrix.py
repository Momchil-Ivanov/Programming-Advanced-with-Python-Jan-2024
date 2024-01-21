rows = int(input())

matrix = []

for row in range(0, rows):
    for el in input().split(', '):
        matrix.append(int(el))

print(matrix)