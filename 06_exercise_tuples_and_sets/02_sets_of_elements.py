first_and_second_set_lenghts = input().split()

first_set_lenght = int(first_and_second_set_lenghts[0])
second_set_lenght = int(first_and_second_set_lenghts[1])

first_set = set()
second_set = set()

for _ in range(first_set_lenght):
    first_set.add(input())

for _ in range(second_set_lenght):
    second_set.add(input())

for common_element in first_set & second_set:
    print(common_element)