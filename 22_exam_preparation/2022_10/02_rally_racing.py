size = int(input())
racing_car_number = input()

matrix = []
car_row = 0
car_col = 0

for row in range(size):
    matrix.append([str(el) for el in input().split(' ')])

matrix[car_row][car_col] = 'C'
kilometers = 0
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

finished = False

while True:
    command = input()
    if command == 'End':
        break

    matrix[car_row][car_col] = '.'

    car_row += directions[command][0]
    car_col += directions[command][1]

    if matrix[car_row][car_col] == '.':
        kilometers += 10
    elif matrix[car_row][car_col] == 'T':
        matrix[car_row][car_col] = '.'
        kilometers += 30
        for row in range(size):
            if 'T' in matrix[row]:
                car_row = row
                car_col = matrix[row].index('T')
    elif matrix[car_row][car_col] == 'F':
        kilometers += 10
        finished = True

    matrix[car_row][car_col] = 'C'
    if finished:
        break

if finished:
    print(f'Racing car {racing_car_number} finished the stage!')
else:
    print(f'Racing car {racing_car_number} DNF.')

print(f'Distance covered {kilometers} km.')

for row in matrix:
    print("".join([str(el) for el in row]))
