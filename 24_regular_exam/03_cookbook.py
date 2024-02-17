def cookbook(*recipes):
    cuisine_dict = {}

    for recipe in recipes:
        name = recipe[0]
        cuisine = recipe[1]
        ingredients = recipe[2]
        sorted_ingredients = sorted(ingredients)
        if cuisine not in cuisine_dict:
            cuisine_dict[cuisine] = {f'{name}': ingredients}
        else:
            cuisine_dict[cuisine].update({f'{name}': ingredients})

    sorted_dict = dict(sorted(cuisine_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    result = ''

    for cuisine in sorted_dict.keys():
        result += f'{cuisine} cuisine contains {len(sorted_dict[cuisine])} recipes:\n'
        cuisine_dict = sorted_dict[cuisine]
        sorted_cuisine_dict = dict(sorted(cuisine_dict.items()))
        # print(sorted_cuisine_dict)
        for key in sorted_cuisine_dict.keys():
            result += f'  * {key} -> Ingredients: {", ".join(sorted_cuisine_dict[key])}\n'

    return result

    # for cuisine in sorted_dict:
    #     print(cuisine)
    #     print()
    #     current_recipes_per_cuisine = sorted_dict[cuisine]
    #
    #     # print(current_recipes_per_cuisine)
    #     current_cuisine_dict = {}
    #     for item in current_recipes_per_cuisine():
    #         mini_dict = item
    #         for recipe_name in mini_dict:
    #             print(recipe_name)
    #             if recipe_name not in current_cuisine_dict:
    #                 current_cuisine_dict[recipe_name] = item[recipe_name]
    #             else:
    #                 current_cuisine_dict[recipe_name] += item[recipe_name]
    #
    #     print(current_cuisine_dict)


# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

# print(cookbook(
#     ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"])
#     ))

# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
#     ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
#     ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
#     ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
#     ))

print(cookbook(
                    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
                      ("Chicken Curry", "Indian", ["chicken", "curry paste", "coconut milk", "rice"]),
                      ("Caesar Salad", "American", ["romaine lettuce", "croutons", "parmesan", "caesar dressing"]),
                      ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
                      ("Mushroom Risotto", "Italian", ["arborio rice", "mushrooms", "onion", "parmesan", "broth"]),
                      ("Tacos", "Mexican", ["tortillas", "ground beef", "lettuce", "tomato", "cheese"]),
                      ("Pad Thai", "Thai", ["rice noodles", "shrimp", "peanuts", "bean sprouts", "tamarind sauce"]),
                      ("Chicken Alfredo", "Italian", ["fettuccine", "chicken", "alfredo sauce", "broccoli"])))