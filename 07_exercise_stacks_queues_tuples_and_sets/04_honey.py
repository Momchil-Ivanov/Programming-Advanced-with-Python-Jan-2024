from collections import deque

bees = deque(int(el) for el in input().split())
nectar = deque(int(el) for el in input().split())
symbols = deque(input().split())

honey = 0

while bees and nectar:
    first_bee = bees.popleft()
    last_nectar = nectar.pop()

    if last_nectar >= first_bee:
        # STEP TWO
        current_symbol = symbols.popleft()

        if current_symbol == "/" and last_nectar == 0:
            continue

        result = str(first_bee) + current_symbol + str(last_nectar)
        honey += abs(eval(result))
    else:
        bees.appendleft(first_bee)
        continue

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(el) for el in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(el) for el in nectar)}")