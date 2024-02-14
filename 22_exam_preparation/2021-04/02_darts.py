size = 7
matrix = []

player_one, player_two = [str(el) for el in input().split(', ')]
player_one_throws = 0
player_two_throws = 0
player_one_points = 501
player_two_points = 501
player_one_wins = False
player_two_wins = False
for row in range(size):
    matrix.append([str(el) for el in input().split()])

while True:
    command = input().split(', ')
    the_row = int(command[0].replace('(', ''))
    the_col = int(command[1].replace(')', ''))

    if not 0 <= the_row < size or not 0 <= the_col < size:
        pass
    else:
        if matrix[the_row][the_col] == 'B':
            player_one_wins = True
            player_one_throws += 1
            break
        elif matrix[the_row][the_col] == 'D':
            player_one_points -= (int(matrix[the_row][0]) + int(matrix[the_row][size - 1]) + int(matrix[0][the_col]) + int(matrix[size - 1][the_col])) * 2
        elif matrix[the_row][the_col] == 'T':
            player_one_points -= (int(matrix[the_row][0]) + int(matrix[the_row][size - 1]) + int(matrix[0][the_col]) + int(matrix[size - 1][the_col])) * 3
        else:
            score = int(matrix[the_row][the_col])
            player_one_points -= score

    player_one_throws += 1

    if player_one_points <= 0:
        player_one_wins = True
        break

    command = input().split(', ')
    the_row = int(command[0].replace('(', ''))
    the_col = int(command[1].replace(')', ''))
    if not 0 <= the_row < size or not 0 <= the_col < size:
        pass
    else:
        if matrix[the_row][the_col] == 'B':
            player_two_wins = True
            player_two_throws += 1
            break
        elif matrix[the_row][the_col] == 'D':
            player_two_points -= (int(matrix[the_row][0]) + int(matrix[the_row][size - 1]) + int(matrix[0][the_col]) + int(matrix[size - 1][the_col])) * 2
        elif matrix[the_row][the_col] == 'T':
            player_two_points -= (int(matrix[the_row][0]) + int(matrix[the_row][size - 1]) + int(matrix[0][the_col]) + int(matrix[size - 1][the_col])) * 3
        else:
            score = int(matrix[the_row][the_col])
            player_two_points -= score

    player_two_throws += 1

    if player_two_points <= 0:
        player_two_wins = True
        break

if player_one_wins:
    print(f'{player_one} won the game with {player_one_throws} throws!')
else:
    print(f'{player_two} won the game with {player_two_throws} throws!')
