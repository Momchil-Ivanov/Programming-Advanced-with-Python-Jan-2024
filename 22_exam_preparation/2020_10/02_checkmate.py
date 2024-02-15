size = 8
matrix = []
winning_queens_positions = []
for row in range(size):
    matrix.append([str(el) for el in input().split()])

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'Q':
            q_row = row
            q_col = col
            # up
            t_row = q_row
            t_col = q_col
            while t_row > 0:
                t_row -= 1
                if matrix[t_row][t_col] == 'Q':
                    break
                elif matrix[t_row][t_col] == 'K':
                    winning_queens_positions.append([q_row, q_col])

            # down
            t_row = q_row
            t_col = q_col
            while t_row < size - 2:
                t_row += 1
                if matrix[t_row][t_col] == 'Q':
                    break
                elif matrix[t_row][t_col] == 'K':
                    winning_queens_positions.append([q_row, q_col])

            # left
            t_row = q_row
            t_col = q_col
            while t_col > 0:
                t_col -= 1
                if matrix[t_row][t_col] == 'Q':
                    break
                elif matrix[t_row][t_col] == 'K':
                    winning_queens_positions.append([q_row, q_col])

            # right
            t_row = q_row
            t_col = q_col
            while t_col < size - 2:
                t_col += 1
                if matrix[t_row][t_col] == 'Q':
                    break
                elif matrix[t_row][t_col] == 'K':
                    winning_queens_positions.append([q_row, q_col])

            # up-left
            t_row = q_row
            t_col = q_col
            while t_row > 0 and t_col > 0:
                t_row -= 1
                t_col -= 1
                if matrix[t_row][t_col] == 'Q':
                    break
                elif matrix[t_row][t_col] == 'K':
                    winning_queens_positions.append([q_row, q_col])

            # down-left
            t_row = q_row
            t_col = q_col
            while t_row < size - 2 and t_col > 0:
                t_row += 1
                t_col -= 1
                if matrix[t_row][t_col] == 'Q':
                    break
                elif matrix[t_row][t_col] == 'K':
                    winning_queens_positions.append([q_row, q_col])

            # up-right
            t_row = q_row
            t_col = q_col
            while t_row > 0 and t_col < size - 2:
                t_row -= 1
                t_col += 1
                if matrix[t_row][t_col] == 'Q':
                    break
                elif matrix[t_row][t_col] == 'K':
                    winning_queens_positions.append([q_row, q_col])

            # down-right
            t_row = q_row
            t_col = q_col
            while t_row < size - 2 and t_col < size - 2:
                t_row += 1
                t_col += 1
                if matrix[t_row][t_col] == 'Q':
                    break
                elif matrix[t_row][t_col] == 'K':
                    winning_queens_positions.append([q_row, q_col])


if winning_queens_positions:
    for position in winning_queens_positions:
        print(position)
else:
    print('The king is safe!')
