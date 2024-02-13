size = 6
matrix = []

for row in range(size):
    matrix.append([str(el) for el in input().split()])

moves = 3
total_sum = 0

for move in range(moves):
    coordinates_list = input().split(', ')
    current_row = int(coordinates_list[0].replace('(', ''))
    current_col = int(coordinates_list[1].replace(')', ''))

    if not 0 <= current_row < size or not 0 <= current_col < size:
        continue

    if matrix[current_row][current_col] == 'B':
        matrix[current_row][current_col] = '0'
        for row in range(size):
            total_sum += int(matrix[row][current_col])

if total_sum < 100:
    print(f'Sorry! You need {100 - total_sum} points more to win a prize.')
elif total_sum >= 300:
    print(f"Good job! You scored {total_sum} points, and you've won Lego Construction Set.")
elif 200 <= total_sum <= 299:
    print(f"Good job! You scored {total_sum} points, and you've won Teddy Bear.")
elif 100 <= total_sum <= 199:
    print(f"Good job! You scored {total_sum} points, and you've won Football.")
