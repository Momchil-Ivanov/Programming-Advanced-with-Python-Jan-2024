n_lines = int(input())

odd_set = set()
even_set = set()

for line_number in range(1, n_lines + 1):
    current_name = input()
    ascii_sum = 0
    for char in current_name:
        ascii_sum += ord(char)
    ascii_result = int(ascii_sum / line_number)
    if ascii_result % 2 == 0:
        even_set.add(ascii_result)
    else:
        odd_set.add(ascii_result)

if sum(odd_set) == sum(even_set):
    union = odd_set | even_set
    # print("union")
    print(', '.join(str(number) for number in union))
elif sum(odd_set) > sum(even_set):
    # print("difference")
    difference = odd_set - even_set
    print(', '.join(str(number) for number in difference))
else:
    # print("symmetric_difference")
    symmetric_difference_even = even_set - odd_set
    symmetric_difference_odd = odd_set - even_set
    symmetric_difference_union = symmetric_difference_even | symmetric_difference_odd
    print(', '.join(str(number) for number in symmetric_difference_union))