rows, cols = [int(el) for el in input().split()]

matrix = []
max_sum = 0
for row in range(0, rows):
    matrix.append([int(el) for el in input().split()])

max_sum = 0
max_first = 0
max_second = 0
max_third = 0
max_forth = 0
max_fifth = 0
max_sixth = 0
max_seventh = 0
max_eighth = 0
max_ninth = 0

for row in range(0, rows - 2):
    for col in range(0, cols - 2):
        first_num = matrix[row][col]
        second_num = matrix[row][col + 1]
        third_num = matrix[row][col + 2]
        forth_num = matrix[row + 1][col]
        fifth_num = matrix[row + 1][col + 1]
        sixth_num = matrix[row + 1][col + 2]
        seventh_num = matrix[row + 2][col]
        eighth_num = matrix[row + 2][col + 1]
        ninth_num = matrix[row + 2][col + 2]

        current_sum = first_num + second_num + third_num + forth_num + fifth_num + sixth_num \
        + seventh_num + eighth_num + ninth_num

        if current_sum > max_sum:
            max_sum = current_sum
            max_first = first_num
            max_second = second_num
            max_third = third_num
            max_forth = forth_num
            max_fifth = fifth_num
            max_sixth = sixth_num
            max_seventh = seventh_num
            max_eighth = eighth_num
            max_ninth = ninth_num

print(f"Sum = {max_sum}")
print(f"{max_first} {max_second} {max_third}")
print(f"{max_forth} {max_fifth} {max_sixth}")
print(f"{max_seventh} {max_eighth} {max_ninth}")