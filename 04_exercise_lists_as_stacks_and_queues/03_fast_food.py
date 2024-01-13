from collections import deque

food_quantity = int(input())
order_list = input().split()
order_list_int = map(int, order_list)

queue = deque()
print(max(order_list_int))

for x in range(0, len(order_list)):
    queue.append(int(order_list[x]))

for y in range(0, len(order_list)):
    if queue[0] <= food_quantity:
        food_quantity -= queue[0]
        queue.popleft()
    else:
        break

if len(queue) == 0:
    print("Orders complete")
else:
    queue = map(str, queue)
    print(f"Orders left: {' '.join(queue)}")