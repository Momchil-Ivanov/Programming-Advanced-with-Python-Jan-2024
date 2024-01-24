size = 5

matrix = [[str(el) for el in input().split()] for row in range(size)]

shooter_row = 0
shooter_col = 0
targets_count = 0
hit_locations = []

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "A":
            shooter_row = row
            shooter_col = col
            matrix[row][col] = "."
        if matrix[row][col] == "x":
            targets_count += 1

targets_count_ini = targets_count
number_of_commands = int(input())

for _ in range(number_of_commands):
    current_command = input().split()

    if current_command[0] == "move":
        spaces = int(current_command[2])
        if current_command[1] == "up":
            if shooter_row - spaces >= 0:
                if matrix[shooter_row - spaces][shooter_col] == ".":
                    shooter_row -= spaces
        elif current_command[1] == "down":
            if shooter_row + spaces < size:
                if matrix[shooter_row + spaces][shooter_col] == ".":
                    shooter_row += spaces
        elif current_command[1] == "left":
            if shooter_col - spaces >= 0:
                if matrix[shooter_row][shooter_col - spaces] == ".":
                    shooter_col -= spaces
        elif current_command[1] == "right":
            if shooter_col + spaces < size:
                if matrix[shooter_row][shooter_col + spaces] == ".":
                    shooter_col += spaces
    elif current_command[0] == "shoot":
        if current_command[1] == "up":
            for row in range(shooter_row, -1, -1):
                if matrix[row][shooter_col] == "x":
                    targets_count -= 1
                    matrix[row][shooter_col] = "."
                    hit_locations.append([row, shooter_col])
                    break
        elif current_command[1] == "down":
            for row in range(shooter_row, size):
                if matrix[row][shooter_col] == "x":
                    targets_count -= 1
                    matrix[row][shooter_col] = "."
                    hit_locations.append([row, shooter_col])
                    break
        elif current_command[1] == "left":
            for col in range(shooter_col, - 1, - 1):
                if matrix[shooter_row][col] == "x":
                    targets_count -= 1
                    matrix[shooter_row][col] = "."
                    hit_locations.append([shooter_row, col])
                    break
        elif current_command[1] == "right":
            for col in range(shooter_col, size):
                if matrix[shooter_row][col] == "x":
                    targets_count -= 1
                    matrix[shooter_row][col] = "."
                    hit_locations.append([shooter_row, col])
                    break

    if targets_count == 0:
        break

if targets_count == 0:
    print(f"Training completed! All {targets_count_ini} targets hit.")
else:
    print(f"Training not completed! {targets_count} targets left.")

for el in hit_locations:
    print(el)