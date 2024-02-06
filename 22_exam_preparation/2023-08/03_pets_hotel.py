def accommodate_new_pets(capacity: int, max_weight: float, *pet_info):
    pet_dict = {}
    pets_left = False
    pets = len(pet_info)

    for pet in pet_info:
        pet_name = pet[0]
        pet_weight = float(pet[1])
        if pet_weight <= max_weight:
            if pet_name not in pet_dict.keys():
                pet_dict[pet_name] = 1
            else:
                pet_dict[pet_name] += 1
            capacity -= 1

        pets -= 1

        if capacity == 0:
            if pets > 0:
                pets_left = True
            break
    result = ''

    if not pets_left:
        result += f'All pets are accommodated! Available capacity: {capacity}.\n'
    else:
        result += f'You did not manage to accommodate all pets!\n'
    result += f'Accommodated pets:\n'
    sorted_pet_dict = dict(sorted(pet_dict.items(), key=lambda kvp: kvp[0]))

    for pet in sorted_pet_dict.keys():
        result += f'{pet}: {sorted_pet_dict[pet]}\n'

    return result


print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))