n_guests = int(input())

vip_list = set()
normal_list = set()

for _ in range(n_guests):
    current_guest = input()
    if current_guest[0].isdigit():
        vip_list.add(current_guest)
    else:
        normal_list.add(current_guest)

while True:
    command = input()

    if command == "END":
        break

    if command in vip_list:
        vip_list.remove(command)
    elif command in normal_list:
        normal_list.remove(command)

count = len(vip_list) + len(normal_list)
print(count)

for guest_vip in sorted(vip_list):
    print(guest_vip)
for guest in sorted(normal_list):
    print(guest)