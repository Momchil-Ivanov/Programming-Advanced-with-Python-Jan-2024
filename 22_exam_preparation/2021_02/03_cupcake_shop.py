from collections import deque

def stock_availability(inventory: list, command: str, *extra_input):
    final_list = deque(inventory)
    if command == 'delivery':
        for box in extra_input:
            final_list.append(box)
    elif command == 'sell':
        if len(extra_input) == 0:
            final_list.popleft()
        elif str(extra_input[0]).isnumeric():
            count = int(extra_input[0])
            for x in range(count):
                final_list.popleft()
        else:
            for item in extra_input:
                while item in final_list:
                    final_list.remove(item)
    final_list = list(final_list)
    return final_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
