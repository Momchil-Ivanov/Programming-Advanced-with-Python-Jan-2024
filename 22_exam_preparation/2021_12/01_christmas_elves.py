from collections import deque

elf_energy = deque([int(el) for el in input().split()])
materials_in_boxes = deque([int(el) for el in input().split()])

toys = 0
energy = 0
turn = 0
while elf_energy and materials_in_boxes:

    first_elf = elf_energy.popleft()
    last_box = materials_in_boxes.pop()
    if first_elf < 5:
        materials_in_boxes.append(last_box)
        continue
    turn += 1

    if turn % 3 == 0:
        if first_elf >= 2 * last_box:
            toys += 2
            energy += 2 * last_box
            first_elf -= 2 * last_box
            first_elf += 1
            if turn % 5 == 0:
                toys -= 2
                first_elf -= 1
            elf_energy.append(first_elf)
        else:
            elf_energy.append(first_elf * 2)
            materials_in_boxes.append(last_box)
    elif first_elf >= last_box:
        toys += 1
        energy += last_box
        first_elf -= last_box
        first_elf += 1
        if turn % 5 == 0:
            toys -= 1
            first_elf -= 1
        elf_energy.append(first_elf)
    else:
        elf_energy.append(first_elf * 2)
        materials_in_boxes.append(last_box)

print(f'Toys: {toys}')
print(f'Energy: {energy}')

if elf_energy:
    print(f'Elves left: {", ".join([str(el) for el in elf_energy])}')
if materials_in_boxes:
    print(f'Boxes left: {", ".join([str(el) for el in materials_in_boxes])}')
