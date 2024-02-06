from collections import deque

worms = deque([int(el) for el in input().split()])
holes = deque([int(el) for el in input().split()])
matches = 0
negative_worm = False

while worms and holes:
    last_worm = worms.pop()
    if last_worm <= 0:
        negative_worm = True
        continue
    first_hole = holes.popleft()

    if last_worm != first_hole:
        worms.append(last_worm - 3)
    else:
        matches += 1

if matches > 0:
    print(f'Matches: {matches}')
else:
    print('There are no matches.')

if len(worms) == 0 and not negative_worm:
    print(f'Every worm found a suitable hole!')
elif len(worms) == 0 and negative_worm:
    print(f'Worms left: none')
else:
    print(f'Worms left: {", ".join([str(el) for el in worms])}')

if len(holes) == 0:
    print('Holes left: none')
else:
    print(f'Holes left: {", ".join([str(el) for el in holes])}')