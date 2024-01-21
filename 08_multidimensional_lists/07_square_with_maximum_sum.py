max_sum = 0
first_index = ""
second_index = ""
third_index = ""
forth_index = ""

rows, cols = [int(el) for el in input().split(', ')]

matrix = []

for row in range(0, rows):
    matrix.append([int(el) for el in input().split(', ')])

for row in range(0, rows - 1):
    for col in range(0, cols - 1):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
        if current_sum > max_sum:
            max_sum = current_sum
            first_index = matrix[row][col]
            second_index = matrix[row][col + 1]
            third_index = matrix[row + 1][col]
            forth_index = matrix[row + 1][col + 1]

print(f"{first_index} {second_index}")
print(f"{third_index} {forth_index}")
print(max_sum)