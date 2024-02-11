from collections import deque

seats_list = input().split(', ')

# seats_dict = {}
#
# for seat in seats_list:
#     number = ""
#     symbol = ""
#     for char in seat:
#         if char.isdigit():
#             number += char
#         else:
#             symbol += char
#
#     seats_dict[symbol] = int(number)

first_sequence = deque([int(el) for el in input().split(', ')])
second_sequence = deque([int(el) for el in input().split(', ')])

matches = 0
matches_list = []
rotations = 0

already_matched = []

while first_sequence and second_sequence and matches < 3 and rotations < 10:
    first_num_first_seq = first_sequence.popleft()
    last_num_second_seq = second_sequence.pop()
    num_sum = first_num_first_seq + last_num_second_seq
    ascii_char = chr(num_sum)
    first_option = f'{first_num_first_seq}{ascii_char}'
    second_option = f'{last_num_second_seq}{ascii_char}'

    if first_option in seats_list:
        if first_option not in already_matched:
            matches += 1
            matches_list.append(first_option)
            already_matched.append(first_option)
    elif second_option in seats_list:
        if second_option not in already_matched:
            matches += 1
            matches_list.append(second_option)
            already_matched.append(second_option)
    else:
        if first_option not in already_matched and second_option not in already_matched:
            first_sequence.append(first_num_first_seq)
            second_sequence.appendleft(last_num_second_seq)

    rotations += 1

print(f'Seat matches: {", ".join(matches_list)}')
print(f'Rotations count: {rotations}')
