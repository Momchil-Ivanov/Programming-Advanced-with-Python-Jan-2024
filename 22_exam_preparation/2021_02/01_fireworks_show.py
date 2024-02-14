from collections import deque

firework_effects = deque([int(el) for el in input().split(', ')])
explosive_power = deque([int(el) for el in input().split(', ')])

palms = 0
willows = 0
crossettes = 0

success = False

while firework_effects and explosive_power:
    first_firework = firework_effects.popleft()
    last_explosive = explosive_power.pop()

    if first_firework <= 0:
        explosive_power.append(last_explosive)
        continue
    elif last_explosive <= 0:
        firework_effects.appendleft(first_firework)
        continue

    current_sum = first_firework + last_explosive

    if current_sum % 3 == 0 and current_sum % 5 != 0:
        palms += 1
    elif current_sum % 5 == 0 and current_sum % 3 != 0:
        willows += 1
    elif current_sum % 3 == 0 and current_sum % 5 == 0:
        crossettes += 1
    else:
        firework_effects.append(first_firework - 1)
        explosive_power.append(last_explosive)

    if palms >= 3 and willows >= 3 and crossettes >= 3:
        success = True
        break

if success:
    print(f'Congrats! You made the perfect firework show!')
else:
    print(f"Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f'Firework Effects left: {", ".join([str(el) for el in firework_effects])}')
if explosive_power:
    print(f'Explosive Power left: {", ".join([str(el) for el in explosive_power])}')

print(f'Palm Fireworks: {palms}')
print(f'Willow Fireworks: {willows}')
print(f'Crossette Fireworks: {crossettes}')
