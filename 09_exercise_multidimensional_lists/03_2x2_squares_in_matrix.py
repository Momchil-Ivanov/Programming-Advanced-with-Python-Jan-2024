two_by_two_squares_count = 0

rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(0, rows):
    matrix.append([str(el) for el in input().split(' ')])

for row in range(0, rows -1):
    for col in range(0, cols - 1):
        first_symbol = matrix[row][col]
        second_symbol = matrix[row][col + 1]
        third_symbol = matrix[row + 1][col]
        forth_symbol = matrix[row + 1][col + 1]

        if first_symbol == second_symbol == third_symbol == forth_symbol:
            two_by_two_squares_count += 1

print(two_by_two_squares_count)