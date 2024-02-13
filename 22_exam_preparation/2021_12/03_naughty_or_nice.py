def naughty_or_nice_list(kids_list: list, *number_status, **name_status):
    kids_list_copy = kids_list.copy()
    nice_list = []
    naughty_list = []
    for number in number_status:
        number_list = number.split('-')
        current_number = int(number_list[0])
        current_status = number_list[1]
        counter = 0
        kid_name = ''
        for item in kids_list_copy:
            if current_number == item[0]:
                counter += 1
                kid_name = item[1]
        if counter == 1:
            if current_status == 'Nice':
                nice_list.append(kid_name)
            elif current_status == 'Naughty':
                naughty_list.append(kid_name)
            kids_list_copy.remove((current_number, kid_name))

    for key in name_status.keys():
        key_status = name_status[key]
        counter = 0
        kid_number = 0
        for item in kids_list_copy:
            if key == item[1]:
                counter += 1
                kid_number = int(item[0])
        if counter == 1:
            if key_status == 'Nice':
                nice_list.append(key)
            elif key_status == 'Naughty':
                naughty_list.append(key)
            kids_list_copy.remove((kid_number, key))

    not_found_list = []
    if kids_list_copy:
        for item in kids_list_copy:
            not_found_list.append(item[1])

    result = ''
    if nice_list:
        result += f'Nice: {", ".join(nice_list)}\n'
    if naughty_list:
        result += f'Naughty: {", ".join(naughty_list)}\n'
    if not_found_list:
        result += f'Not found: {", ".join(not_found_list)}'

    if result != '':
        return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

print()

print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print()

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))

print()

print(naughty_or_nice_list(
    []
))