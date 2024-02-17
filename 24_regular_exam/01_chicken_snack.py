from collections import deque

amount_of_money_size = deque([int(el) for el in input().split()])
price_size = deque([int(el) for el in input().split()])
food_eaten = 0
change = 0
while amount_of_money_size and price_size:
    last_money = amount_of_money_size.pop()
    if change > 0:
        last_money += change
        change = 0
    first_price = price_size.popleft()

    if last_money == first_price:
        food_eaten += 1
    elif last_money > first_price:
        food_eaten += 1
        change = last_money - first_price

if food_eaten >= 4:
    print(f'Gluttony of the day! Henry ate {food_eaten} foods.')
elif food_eaten > 1:
    print(f'Henry ate: {food_eaten} foods.')
elif food_eaten == 1:
    print(f'Henry ate: {food_eaten} food.')
elif food_eaten == 0:
    print(f'Henry remained hungry. He will try next weekend again.')
