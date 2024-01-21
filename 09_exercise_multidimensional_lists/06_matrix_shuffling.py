rows, cols = [int(el) for el in input().split()]

matrix = []

for row in range(0, rows):
    matrix.append([str(el) for el in input().split()])

while True:
    command_list = input().split()
    current_command = command_list[0]
    if current_command == "END":
        break
    if current_command != "swap" or len(command_list) != 5:
        print(f"Invalid input!")
        continue

    row_one = int(command_list[1])
    col_one = int(command_list[2])
    row_two = int(command_list[3])
    col_two = int(command_list[4])

    if row_one >= rows or row_two >= rows or col_one >= cols or col_two >= cols:
        print(f"Invalid input!")
        continue

    first_value = matrix[row_one][col_one]
    second_value = matrix[row_two][col_two]

    matrix[row_one][col_one] = second_value
    matrix[row_two][col_two] = first_value

    for row in matrix:
        print(' '.join(row))