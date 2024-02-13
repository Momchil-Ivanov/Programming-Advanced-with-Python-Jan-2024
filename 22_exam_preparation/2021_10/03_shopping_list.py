def shopping_list(budget: int, **items_info):
    current_budget = budget
    if current_budget < 100:
        return f'You do not have enough budget.'
    counter = 0
    result = ''
    for key in items_info:
        current_price = float(items_info[key][0])
        current_quantity = int(items_info[key][1])
        total_current_price = current_price * current_quantity
        if current_budget >= total_current_price:
            current_budget -= total_current_price
            result += f'You bought {key} for {total_current_price:.2f} leva.\n'
            counter += 1
        if counter == 5:
            break

    return result


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))

# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
