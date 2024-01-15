n_lines = int(input())

periodic_set = set()

for _ in range(n_lines):
    current_elements = input().split()

    for element in current_elements:
        periodic_set.add(element)

for item in periodic_set:
    print(item)