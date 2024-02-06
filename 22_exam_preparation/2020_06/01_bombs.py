from collections import deque

bomb_effects = deque([int(el) for el in input().split(', ')])
bomb_casings = deque([int(el) for el in input().split(', ')])

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0

pouch_filled = False

while len(bomb_effects) > 0 and len(bomb_casings) > 0:
    first_bomb_effect = bomb_effects.popleft()
    last_bomb_casing = bomb_casings.pop()

    values_sum = first_bomb_effect + last_bomb_casing
    if values_sum == 40 or values_sum == 60 or values_sum == 120:
        if values_sum == 40:
            datura_bombs += 1
        elif values_sum == 60:
            cherry_bombs += 1
        elif values_sum == 120:
            smoke_decoy_bombs += 1
    else:
        bomb_effects.appendleft(first_bomb_effect)
        bomb_casings.append(last_bomb_casing - 5)

    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        pouch_filled = True
        break

if pouch_filled:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

bomb_effects_result = ''
if len(bomb_effects) == 0:
    bomb_effects_result = 'empty'
else:
    bomb_effects_result = ', '.join([str(el) for el in bomb_effects])

bomb_casings_result = ''
if len(bomb_casings) == 0:
    bomb_casings_result = 'empty'
else:
    bomb_casings_result = ', '.join([str(el) for el in bomb_casings])

print(f'Bomb Effects: {bomb_effects_result}')
print(f'Bomb Casings: {bomb_casings_result}')

print(f'Cherry Bombs: {cherry_bombs}')
print(f'Datura Bombs: {datura_bombs}')
print(f'Smoke Decoy Bombs: {smoke_decoy_bombs}')