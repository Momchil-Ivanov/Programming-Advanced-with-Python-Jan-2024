def grocery_store(**kwargs):
    result =''
    sorted_result = sorted(
        kwargs.items(),
        key=lambda kvp: (-int(kvp[1]), -len(kvp[0]), kvp[0])
    )
    for product_name, quantities in sorted_result:
        result += f"{product_name}: {quantities}\n"

    return result

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))