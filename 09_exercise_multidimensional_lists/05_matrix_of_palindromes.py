rows, cols = [int(el) for el in input().split()]

line = []

for row in range(0, rows):
    first_and_last_char = chr(row + 97)
    for col in range(0, cols):
        middle_char = chr(col + 97 + row)
        current_string = first_and_last_char + middle_char + first_and_last_char
        line.append(current_string)
    print(' '.join(line))
    line = []