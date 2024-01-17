from collections import deque

materials = deque(int(el) for el in input().split())
magic_level = deque(int(el) for el in input().split())

doll_count = 0
wooden_train_count = 0
teddy_bear_count = 0
bicycle_count = 0

task_completed = False

while materials and magic_level:
    last_material = materials.pop()
    first_magic_level = magic_level.popleft()

    total_magic_level = last_material * first_magic_level
    if total_magic_level == 150:
        doll_count += 1
    elif total_magic_level == 250:
        wooden_train_count += 1
    elif total_magic_level == 300:
        teddy_bear_count += 1
    elif total_magic_level == 400:
        bicycle_count += 1
    elif total_magic_level < 0:
        materials.append(last_material + first_magic_level)
    elif total_magic_level > 0:
        materials.append(last_material + 15)
    elif total_magic_level == 0:
        if last_material == 0 and first_magic_level == 0:
            continue
        elif last_material == 0:
            magic_level.appendleft(first_magic_level)
        elif first_magic_level == 0:
            materials.append(last_material)

if (doll_count > 0 and wooden_train_count > 0) or (teddy_bear_count > 0 and bicycle_count > 0):
    task_completed = True

if task_completed:
    print(f"The presents are crafted! Merry Christmas!")
else:
    print(f"No presents this Christmas!")

if materials:
    materials_reversed = deque()
    for _ in range(len(materials)):
        materials_reversed.append(materials.pop())
    print(f"Materials left: {', '.join(str(el) for el in materials_reversed)}")
if magic_level:
    print(f"Magic left: {', '.join(str(el) for el in magic_level)}")

if bicycle_count > 0:
    print(f"Bicycle: {bicycle_count}")
if doll_count > 0:
    print(f"Doll: {doll_count}")
if teddy_bear_count > 0:
    print(f"Teddy bear: {teddy_bear_count}")
if wooden_train_count > 0:
    print(f"Wooden train: {wooden_train_count}")