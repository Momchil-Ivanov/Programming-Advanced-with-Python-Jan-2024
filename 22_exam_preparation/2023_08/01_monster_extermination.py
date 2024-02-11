from collections import deque

monsters_armor = deque([int(el) for el in input().split(',')])
soldier_strikes = deque([int(el) for el in input().split(',')])
killed_monsters = 0

while monsters_armor and soldier_strikes:
    first_monster_armor = monsters_armor.popleft()
    last_soldier_strike = soldier_strikes.pop()

    if last_soldier_strike > first_monster_armor:
        killed_monsters += 1
        if soldier_strikes:
            soldier_strikes[-1] += (last_soldier_strike - first_monster_armor)
        else:
            soldier_strikes.append(last_soldier_strike - first_monster_armor)
    elif last_soldier_strike < first_monster_armor:
        monsters_armor.append(first_monster_armor - last_soldier_strike)
    else:
        killed_monsters += 1

if not monsters_armor:
    print(f"All monsters have been killed!")
if not soldier_strikes:
    print(f"The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
