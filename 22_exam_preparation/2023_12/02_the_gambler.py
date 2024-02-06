size = int(input())
amount = 100

matrix = []
gambler_row = 0
gambler_col = 0

for row in range(size):
    matrix.append([el for el in input()])
    if "G" in matrix[row]:
        gambler_row = row
        gambler_col = matrix[row].index("G")

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

game_over = False
out_of_money = False
jackpot = False

while True:
    command = input()
    if command == 'end':
        break
    matrix[gambler_row][gambler_col] = "-"

    gambler_row += directions[command][0]
    gambler_col += directions[command][1]

    if not (0 <= gambler_row < size and 0 <= gambler_col < size):
        game_over = True
        break

    if matrix[gambler_row][gambler_col] == 'W':
        amount += 100
    elif matrix[gambler_row][gambler_col] == 'P':
        amount -= 200
        if amount <= 0:
            out_of_money = True
    elif matrix[gambler_row][gambler_col] == 'J':
        amount += 100000
        jackpot = True

    matrix[gambler_row][gambler_col] = "G"
    if out_of_money or jackpot:
        break

if game_over or out_of_money:
    print(f'Game over! You lost everything!')
else:
    if jackpot:
        print('You win the Jackpot!')
        print(f'End of the game. Total amount: {amount}$')
    elif not jackpot and not out_of_money:
        print(f'End of the game. Total amount: {amount}$')
    for row in matrix:
        print(''.join(str(el) for el in row))