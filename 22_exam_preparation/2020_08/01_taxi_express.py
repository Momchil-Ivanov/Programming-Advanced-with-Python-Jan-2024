from collections import deque

customers = deque([int(el) for el in input().split(', ')])
taxis = deque([int(el) for el in input().split(', ')])

drive_time = 0

while len(customers) > 0 and len(taxis) > 0:
    first_customer = customers.popleft()
    last_taxi = taxis.pop()

    if last_taxi >= first_customer:
        drive_time += first_customer
    else:
        customers.appendleft(first_customer)

if len(customers) == 0:
    print('All customers were driven to their destinations')
    print(f'Total time: {drive_time} minutes')
else:
    print(f'Not all customers were driven to their destinations')
    print(f'Customers left: {", ".join([str(el) for el in customers])}')