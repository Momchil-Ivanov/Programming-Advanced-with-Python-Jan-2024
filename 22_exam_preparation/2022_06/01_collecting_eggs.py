from collections import deque

egg_sizes = deque([int(el) for el in input().split(', ')])
paper_sizes = deque([int(el) for el in input().split(', ')])

filled_boxes = 0

while egg_sizes and paper_sizes:
    first_egg = egg_sizes.popleft()
    last_paper = paper_sizes.pop()

    if first_egg <= 0:
        paper_sizes.append(last_paper)
    elif first_egg == 13:
        first_paper = paper_sizes.popleft()
        paper_sizes.appendleft(last_paper)
        paper_sizes.append(first_paper)
    elif first_egg + last_paper <= 50:
        filled_boxes += 1

if filled_boxes:
    print(f'Great! You filled {filled_boxes} boxes.')
else:
    print(f"Sorry! You couldn't fill any boxes!")

if egg_sizes:
    print(f'Eggs left: {", ".join([str(el) for el in egg_sizes])}')
if paper_sizes:
    print(f'Pieces of paper left: {", ".join([str(el) for el in paper_sizes])}')
