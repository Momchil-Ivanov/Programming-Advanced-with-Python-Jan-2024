size = int(input())

matrix = [[str(el) for el in input().split()] for row in range(size)]

alice_position_row = 0
alice_position_col = 0
alice_found = False
tea_quantity = 0

for row in range(0, size):
    for col in range(0, size):
        if matrix[row][col] == "A":
            alice_position_row, alice_position_col = row, col
            matrix[row][col] = "*"
            alice_found = True
            break
    if alice_found:
        break

alice_failed = False

while True:
    command = input()
    if command == "left":
        if alice_position_col - 1 < 0:
            alice_failed = True
            break
        else:
            matrix[alice_position_row][alice_position_col] = "*"
            alice_position_col -= 1
    elif command == "right":
        if alice_position_col + 1 == size:
            alice_failed = True
            break
        else:
            matrix[alice_position_row][alice_position_col] = "*"
            alice_position_col += 1
    elif command == "up":
        if alice_position_row - 1 < 0:
            alice_failed = True
            break
        else:
            matrix[alice_position_row][alice_position_col] = "*"
            alice_position_row -= 1
    elif command == "down":
        if alice_position_row + 1 == size:
            alice_failed = True
            break
        else:
            matrix[alice_position_row][alice_position_col] = "*"
            alice_position_row += 1

    if matrix[alice_position_row][alice_position_col] == "R":
        matrix[alice_position_row][alice_position_col] = "*"
        alice_failed = True
        break
    elif matrix[alice_position_row][alice_position_col] != "." and matrix[alice_position_row][alice_position_col] != "*":
        tea_value = int(matrix[alice_position_row][alice_position_col])
        tea_quantity += tea_value
        matrix[alice_position_row][alice_position_col] = "*"
        if tea_quantity >= 10:
            break
    else:
        matrix[alice_position_row][alice_position_col] = "A"

if alice_failed:
    print(f"Alice didn't make it to the tea party.")
else:
    print(f"She did it! She went to the party.")

for row in matrix:
    print(*(row))