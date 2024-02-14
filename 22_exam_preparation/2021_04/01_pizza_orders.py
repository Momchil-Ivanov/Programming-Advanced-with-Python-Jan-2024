from collections import deque

pizza_orders = deque([int(el) for el in input().split(', ')])
employees = deque([int(el) for el in input().split(', ')])

total_pizza_made = 0

while pizza_orders and employees:
    first_order = pizza_orders.popleft()
    last_employee = employees.pop()

    if first_order <= 0 or first_order > 10:
        employees.append(last_employee)
        continue

    if first_order > last_employee:
        pizza_left = first_order - last_employee
        first_order = last_employee
        pizza_orders.appendleft(pizza_left)

    total_pizza_made += first_order

if not pizza_orders:
    print(f'All orders are successfully completed!')
    print(f'Total pizzas made: {total_pizza_made}')
    print(f'Employees: {", ".join([str(el) for el in employees])}')
elif not employees and pizza_orders:
    print(f'Not all orders are completed.')
    print(f'Orders left: {", ".join([str(el) for el in pizza_orders])}')
