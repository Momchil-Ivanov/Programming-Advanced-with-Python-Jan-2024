from collections import deque

textiles = deque([int(el) for el in input().split()])
medicaments = deque([int(el) for el in input().split()])

patches = 0
bandages = 0
medkits = 0

while textiles and medicaments:
    first_textile = textiles.popleft()
    last_medicament = medicaments.pop()

    sum_values = first_textile + last_medicament
    if sum_values == 30:
        patches += 1
    elif sum_values == 40:
        bandages += 1
    elif sum_values == 100:
        medkits += 1
    elif sum_values > 100:
        medkits += 1
        second_last_medicament = medicaments.pop()
        medicaments.append(second_last_medicament + sum_values - 100)
    else:
        medicaments.append(last_medicament + 10)

if not textiles and not medicaments:
    print(f'Textiles and medicaments are both empty.')
elif not textiles:
    print(f'Textiles are empty.')
elif not medicaments:
    print(f'Medicaments are empty.')

items_dict = {
    'Patch': patches,
    'Bandage': bandages,
    'MedKit': medkits
}

sorted_dict = sorted(items_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))

for kvp in sorted_dict:
    if kvp[1] != 0:
        print(f'{kvp[0]} - {kvp[1]}')


if textiles:
    print(f'Textiles left: {", ".join([str(el) for el in textiles])}')
elif medicaments:
    medicaments.reverse()
    print(f'Medicaments left: {", ".join([str(el) for el in medicaments])}')
