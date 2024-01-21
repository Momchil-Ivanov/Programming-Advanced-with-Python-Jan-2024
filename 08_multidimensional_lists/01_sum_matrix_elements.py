rows, columns = [int(el) for el in input().split(', ')]
matrix = []
total_sum = 0
for row in range(0, rows):
    raw_data = [int(el) for el in input().split(', ')]
    matrix.append(raw_data)
    total_sum += sum(raw_data)

print(total_sum)
print(matrix)