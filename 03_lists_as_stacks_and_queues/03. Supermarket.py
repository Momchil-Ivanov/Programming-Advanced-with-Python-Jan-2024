from collections import deque

command = input()
current_queue = deque([])

while command != "End":
    if command != "Paid":
        current_queue.append(command)
    else:
        while len(current_queue) > 0:
            print(current_queue.popleft())
    command = input()

print(f"{len(current_queue)} people remaining.")