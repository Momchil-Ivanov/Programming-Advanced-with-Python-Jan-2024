players = [str(el) for el in input().split(', ')]
size = 6

matrix = []

for row in range(size):
    matrix.append([str(el) for el in input().split()])

tom_hit = False
jerry_hit = False

while True:
    current_player = players[0]

    coordinates_list = input().split(', ')
    row_cords = int(coordinates_list[0].replace('(', ''))
    col_cords = int(coordinates_list[1].replace(')', ''))

    if current_player == 'Tom' and tom_hit:
        tom_hit = False
        players.reverse()
        continue
    elif current_player == 'Jerry' and jerry_hit:
        jerry_hit = False
        players.reverse()
        continue

    if matrix[row_cords][col_cords] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break
    elif matrix[row_cords][col_cords] == 'T':
        print(f"{current_player} is out of the game! The winner is {players[1]}.")
        break
    elif matrix[row_cords][col_cords] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        if current_player == 'Tom':
            tom_hit = True
        elif current_player == 'Jerry':
            jerry_hit = True

    players.reverse()
