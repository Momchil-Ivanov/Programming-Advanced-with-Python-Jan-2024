from collections import deque

rows, cols = [int(el) for el in input().split(' ')]

snake_string = input()
snake_string_to_deque = deque()
for el in snake_string:
    snake_string_to_deque.append(el)

line = deque()

for row in range(0, rows):
    if row % 2 == 0:
        for col in range(0, cols):
            current_symbol = snake_string_to_deque.popleft()
            snake_string_to_deque.append(current_symbol)
            line.append(current_symbol)
    else:
        for col in range(0, cols):
            current_symbol = snake_string_to_deque.popleft()
            snake_string_to_deque.append(current_symbol)
            line.appendleft(current_symbol)

    print(''.join(line))
    line = deque()