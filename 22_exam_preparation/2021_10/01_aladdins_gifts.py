from collections import deque

materials = deque([int(el) for el in input().split()])
magic_levels = deque([int(el) for el in input().split()])

gemstones = 0
porcelain_sculptures = 0
gold = 0
diamond_jewellery = 0

while materials and magic_levels:
    last_material = materials.pop()
    first_magic = magic_levels.popleft()
    material_magic_sum = last_material + first_magic

    if material_magic_sum < 100:
        if material_magic_sum % 2 == 0:
            last_material *= 2
            first_magic *= 3
            material_magic_sum = last_material + first_magic
        else:
            material_magic_sum *= 2
    elif material_magic_sum > 499:
        material_magic_sum /= 2

    if 100 <= material_magic_sum <= 199:
        gemstones += 1
    elif 200 <= material_magic_sum <= 299:
        porcelain_sculptures += 1
    elif 300 <= material_magic_sum <= 399:
        gold += 1
    elif 400 <= material_magic_sum <= 499:
        diamond_jewellery += 1

if (gemstones and porcelain_sculptures) or (gold and diamond_jewellery):
    print(f'The wedding presents are made!')
else:
    print(f'Aladdin does not have enough wedding presents.')

if materials:
    print(f'Materials left: {", ".join(str(el) for el in materials)}')
if magic_levels:
    print(f'Magic left: {", ".join(str(el) for el in magic_levels)}')

if diamond_jewellery > 0:
    print(f'Diamond Jewellery: {diamond_jewellery}')
if gemstones > 0:
    print(f'Gemstone: {gemstones}')
if gold > 0:
    print(f'Gold: {gold}')
if porcelain_sculptures > 0:
    print(f'Porcelain Sculpture: {porcelain_sculptures}')
