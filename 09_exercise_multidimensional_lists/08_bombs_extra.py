rows = int(input())
cols = rows

matrix = []

for row in range(0, rows):
    matrix.append([int(el) for el in input().split(' ')])

coordinates = input().split(' ')

for coordinate in coordinates:
    coordinate_to_list = coordinate.split(',')
    row_coordinate = int(coordinate_to_list[0])
    col_coordinate = int(coordinate_to_list[1])
    kaboom_value = matrix[row_coordinate][col_coordinate]
    if kaboom_value <= 0:
        continue
    else:
        try:
            if matrix[row_coordinate - 1][col_coordinate - 1] > 0 and row_coordinate - 1 >= 0 and col_coordinate - 1 >= 0:
                matrix[row_coordinate - 1][col_coordinate - 1] -= kaboom_value
        except:
            pass
        try:
            if matrix[row_coordinate - 1][col_coordinate] > 0 and row_coordinate - 1 >= 0:
                matrix[row_coordinate - 1][col_coordinate] -= kaboom_value
        except:
            pass
        try:
            if matrix[row_coordinate - 1][col_coordinate + 1] > 0 and row_coordinate - 1 >= 0:
                matrix[row_coordinate - 1][col_coordinate + 1] -= kaboom_value
        except:
            pass

        try:
            if matrix[row_coordinate][col_coordinate - 1] > 0 and col_coordinate - 1 >= 0:
                matrix[row_coordinate][col_coordinate - 1] -= kaboom_value
        except:
            pass
        matrix[row_coordinate][col_coordinate] -= kaboom_value
        try:
            if matrix[row_coordinate][col_coordinate + 1] > 0:
                matrix[row_coordinate][col_coordinate + 1] -= kaboom_value
        except:
            pass

        try:
            if matrix[row_coordinate + 1][col_coordinate - 1] > 0 and col_coordinate - 1 >= 0:
                matrix[row_coordinate + 1][col_coordinate - 1] -= kaboom_value
        except:
            pass
        try:
            if matrix[row_coordinate + 1][col_coordinate] > 0:
                matrix[row_coordinate + 1][col_coordinate] -= kaboom_value
        except:
            pass
        try:
            if matrix[row_coordinate + 1][col_coordinate + 1] > 0:
                matrix[row_coordinate + 1][col_coordinate + 1] -= kaboom_value
        except:
            pass

alive_cells = 0
sum_of_alive_cells = 0

for row in range(0, rows):
    for col in range(0, cols):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum_of_alive_cells += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")
for row in matrix:
    print(' '.join([str(el) for el in row]))