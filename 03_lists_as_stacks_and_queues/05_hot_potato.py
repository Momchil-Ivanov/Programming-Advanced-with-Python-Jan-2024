from collections import deque

kids = deque(input().split())

counter = int(input())

while len(kids) > 1:
    for x in range(counter - 1):
        kids.append(kids.popleft())
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.popleft()}")