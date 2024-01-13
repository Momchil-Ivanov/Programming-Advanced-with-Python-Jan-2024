from collections import deque

cups_with_capacity = deque([int(i) for i in input().split()])
bottles_with_capacity = deque([int(o) for o in input().split()])

wasted_liters = 0

while cups_with_capacity and bottles_with_capacity:
    current_bottle = int(bottles_with_capacity.pop())
    if cups_with_capacity[0] - current_bottle <= 0:
        wasted_liters += current_bottle - cups_with_capacity[0]
        cups_with_capacity.popleft()
    else:
        cups_with_capacity[0] -= current_bottle

if len(cups_with_capacity) == 0:
    bottles_from_last_to_fisrt = []
    while bottles_with_capacity:
        bottles_from_last_to_fisrt.append(str(bottles_with_capacity.pop()))
    print(f"Bottles: {' '.join(bottles_from_last_to_fisrt)}")
else:
    cups_with_capacity = [str(z) for z in cups_with_capacity]
    print(f"Cups: {' '.join(cups_with_capacity)}")

print(f"Wasted litters of water: {wasted_liters}")