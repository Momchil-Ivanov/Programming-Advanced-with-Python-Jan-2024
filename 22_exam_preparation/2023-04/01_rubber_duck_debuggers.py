from collections import deque

times_for_tasks = deque([int(el) for el in input().split()])
number_of_tasks = deque([int(el) for el in input().split()])

darth_vader_ducks = 0
thor_ducks = 0
blue_ducks = 0
yellow_ducks = 0

while times_for_tasks and number_of_tasks:
    first_time = times_for_tasks.popleft()
    last_task = number_of_tasks.pop()

    multiplied = first_time * last_task
    if multiplied > 240:
        number_of_tasks.append(last_task - 2)
        times_for_tasks.append(first_time)
    else:
        if 0 <= multiplied <= 60:
            darth_vader_ducks += 1
        elif 61 <= multiplied <= 120:
            thor_ducks += 1
        elif 121 <= multiplied <= 180:
            blue_ducks += 1
        elif 181 <= multiplied <= 240:
            yellow_ducks += 1

print(f'Congratulations, all tasks have been completed! Rubber ducks rewarded:')
print(f'Darth Vader Ducky: {darth_vader_ducks}')
print(f'Thor Ducky: {thor_ducks}')
print(f'Big Blue Rubber Ducky: {blue_ducks}')
print(f'Small Yellow Rubber Ducky: {yellow_ducks}')
