from collections import deque

initial_fuel = deque([int(el) for el in input().split()])
additional_consumption_index = deque([int(el) for el in input().split()])
amount_of_fuel_needed = deque([int(el) for el in input().split()])

reached_altitudes = []
lost = False

for altitude in range(1, len(amount_of_fuel_needed) + 1):
    last_fuel = initial_fuel.pop()
    first_consumption_index = additional_consumption_index.popleft()
    first_amount_of_fuel_needed = amount_of_fuel_needed.popleft()

    difference = last_fuel - first_consumption_index

    if difference >= first_amount_of_fuel_needed:
        print(f'John has reached: Altitude {altitude}')
        reached_altitudes.append(f'Altitude {altitude}')
    else:
        print(f'John did not reach: Altitude {altitude}')
        lost = True
        break

if lost:
    print(f'John failed to reach the top.')
    if len(reached_altitudes) > 0:
        print(f'Reached altitudes: {", ".join(reached_altitudes)}')
    else:
        print(f"John didn't reach any altitude.")
else:
    print(f'John has reached all the altitudes and managed to reach the top!')