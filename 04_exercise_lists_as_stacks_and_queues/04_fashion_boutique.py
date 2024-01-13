racks_count = 1

clothes_in_box = input().split()
rack_capacity = int(input())
max_capacity = int(rack_capacity)

while len(clothes_in_box) > 0:
    current_item = int(clothes_in_box[len(clothes_in_box) - 1])
    if rack_capacity >= current_item:
        rack_capacity -= current_item
        clothes_in_box.pop()
    else:
        racks_count += 1
        rack_capacity = max_capacity

print(racks_count)