from collections import deque

milligrams_of_caffeine = deque([int(el) for el in input().split(', ')])
energy_drinks = deque([int(el) for el in input().split(', ')])

max_caffeine = 300

while milligrams_of_caffeine and energy_drinks:
    last_milligrams_of_caffeine = milligrams_of_caffeine.pop()
    first_energy_drink = energy_drinks.popleft()

    multiplied = last_milligrams_of_caffeine * first_energy_drink
    if multiplied <= max_caffeine:
        max_caffeine -= multiplied
    else:
        energy_drinks.append(first_energy_drink)
        max_caffeine += 30
        if max_caffeine > 300:
            max_caffeine = 300


if energy_drinks:
    print(f'Drinks left: {", ".join([str(el) for el in energy_drinks])}')
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {300 - max_caffeine} mg caffeine.')
