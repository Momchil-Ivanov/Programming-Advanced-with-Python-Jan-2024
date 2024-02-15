from collections import deque

males = deque([int(el) for el in input().split()])
females = deque([int(el) for el in input().split()])

matches = 0

while males and females:
    first_female = females.popleft()
    last_male = males.pop()

    if first_female <= 0:
        males.append(last_male)
        continue
    elif last_male <= 0:
        females.appendleft(first_female)
        continue

    if first_female % 25 == 0:
        if females:
            females.popleft()
            males.append(last_male)
        continue
    elif last_male % 25 == 0:
        if males:
            males.pop()
        females.appendleft(first_female)
        continue

    if first_female == last_male:
        matches += 1
    else:
        males.append(last_male - 2)

print(f"Matches: {matches}")

if males:
    males = reversed(males)
    print(f'Males left: {", ".join([str(el) for el in males])}')
else:
    print(f'Males left: none')

if females:
    print(f'Females left: {", ".join([str(el) for el in females])}')
else:
    print(f'Females left: none')
