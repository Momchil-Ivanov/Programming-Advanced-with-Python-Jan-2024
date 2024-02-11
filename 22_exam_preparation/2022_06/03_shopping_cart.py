def shopping_cart(*products_info):
    products_dict = {
        'Pizza': [],
        'Soup': [],
        'Dessert': []
    }

    for product in products_info:
        if product == "Stop":
            break
        category = product[0]
        ingredient = product[1]

        if category == 'Pizza' and len(products_dict['Pizza']) == 4:
            continue
        elif category == 'Soup' and len(products_dict['Soup']) == 3:
            continue
        elif category == 'Dessert' and len(products_dict['Dessert']) == 2:
            continue

        if ingredient not in products_dict[category]:
            products_dict[category].append(ingredient)

    for key in products_dict.keys():
        products_dict[key] = sorted(products_dict[key])

    sorted_products_dict = dict(sorted(products_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    result = ''
    if len(products_dict['Pizza']) == 0 and len(products_dict['Soup']) == 0 and len(products_dict['Dessert']) == 0:
        result = 'No products in the cart!'
    else:
        for key in sorted_products_dict.keys():
            result += f'{key}:\n'
            for item in sorted_products_dict[key]:
                result += f' - {item}\n'

    return result


# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))

# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))

# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))
