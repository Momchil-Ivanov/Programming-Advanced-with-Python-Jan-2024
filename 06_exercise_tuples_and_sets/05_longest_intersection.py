n_lines = int(input())

intersections = []

for _ in range(n_lines):
    current_input = input().split("-")
    first_range_info = current_input[0].split(",")
    second_range_info = current_input[1].split(",")
    first_start = int(first_range_info[0])
    first_end = int(first_range_info[1])
    second_start = int(second_range_info[0])
    second_end = int(second_range_info[1])

    first_range = set()
    second_range = set()

    for number in range(first_start, first_end + 1):
        first_range.add(number)
    for number in range(second_start, second_end + 1):
        second_range.add(number)

    intersections.append(first_range & second_range)

longest_intersection_index = 0
maximum_length = 0

for index in range(0, len(intersections)):
    if len(intersections[index]) > maximum_length:
        maximum_length = len(intersections[index])
        longest_intersection_index = index

print(f"Longest intersection is [{', '.join(str(x) for x in intersections[longest_intersection_index])}] \
with length {maximum_length}")