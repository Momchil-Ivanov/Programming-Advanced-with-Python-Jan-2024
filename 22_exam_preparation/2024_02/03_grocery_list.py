def shop_from_grocery_list(budget: int, grocery_list: list, *product_info):
    bought_products = []
    money_left = float(budget)

    for product in product_info:
        name = product[0]
        price = float(product[1])
        if name in grocery_list:
            if name not in bought_products:
                if price > money_left:
                    break
                else:
                    money_left -= price
                    bought_products.append(name)
    result = ''

    if len(bought_products) == len(grocery_list):
        result += f'Shopping is successful. Remaining budget: {money_left:.2f}.'
    else:
        missing_products = []
        for product in grocery_list:
            if product not in bought_products:
                missing_products.append(product)
        result += f'You did not buy all the products. Missing products: {", ".join(missing_products)}.'

    return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
