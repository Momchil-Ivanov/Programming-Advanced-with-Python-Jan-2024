from collections import deque

milkshakes = 0

chocolates = deque(int(el) for el in input().split(", "))
cups_of_milk = deque(int(el) for el in input().split(", "))

while milkshakes < 5 and chocolates and cups_of_milk:
    current_chocolate = int(chocolates.pop())
    current_cup = int(cups_of_milk.popleft())

    if current_chocolate <= 0 and current_cup <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup)
        continue
    elif current_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_cup:
        milkshakes += 1
    else:
        chocolates.append(current_chocolate - 5)
        cups_of_milk.append(current_cup)

if milkshakes == 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(el) for el in chocolates)}")
else:
    print(f"Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(el) for el in cups_of_milk)}")
else:
    print(f"Milk: empty")