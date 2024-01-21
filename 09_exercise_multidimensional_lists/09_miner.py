rows = int(input())
cols = rows

command_list = input().split(' ')

matrix = []
miner_position = ""
for row in range(0, rows):
    matrix.append([str(el) for el in input().split(' ')])

miner_row_index = 0
miner_col_index = 0
coal = 0

for row in range(0, rows):
    for col in range(0, cols):
        if matrix[row][col] == "s":
            miner_row_index = row
            miner_col_index = col
        if matrix[row][col] == "c":
            coal += 1


for command in command_list:

    matrix[miner_row_index][miner_col_index] = "*"

    if command == "left":
        if miner_col_index - 1 < 0:
            pass
        else:
            miner_col_index -= 1
    elif command == "right":
        if miner_col_index + 1 >= cols:
            pass
        else:
            miner_col_index += 1
    elif command == "up":
        if miner_row_index - 1 < 0:
            pass
        else:
            miner_row_index -= 1
    elif command == "down":
        if miner_row_index + 1 >= rows:
            pass
        else:
            miner_row_index += 1

    if matrix[miner_row_index][miner_col_index] == "e":
        print(f"Game over! ({miner_row_index}, {miner_col_index})")
        quit()

    if matrix[miner_row_index][miner_col_index] == "c":
        coal -= 1
        if coal == 0:
            print(f"You collected all coal! ({miner_row_index}, {miner_col_index})")
            quit()

    matrix[miner_row_index][miner_col_index] = "s"

print(f"{coal} pieces of coal left. ({miner_row_index}, {miner_col_index})")