rows = int(input())
cols = rows

matrix = [[int(el) for el in input().split()] for row in range(rows)]

command = input()

while command != "END":
    command_to_list = command.split()
    current_command = command_to_list[0]
    row_index = int(command_to_list[1])
    col_index = int(command_to_list[2])

    if row_index < 0 or row_index >= rows or col_index < 0 or col_index >= cols:
        print(f"Invalid coordinates")
    else:
        value = int(command_to_list[3])
        if current_command == "Add":
            matrix[row_index][col_index] += value
        elif current_command == "Subtract":
            matrix[row_index][col_index] -= value

    command = input()

for row in matrix:
    row_to_string = [str(el) for el in row]
    print(' '.join(row_to_string))