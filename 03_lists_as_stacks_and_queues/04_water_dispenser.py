from collections import deque
people = deque([])
capacity_liters = int(input())

person = input()

while person != "Start":
    people.append(person)
    person = input()

command = input()

while command != "End":
    command_to_list = command.split()
    if command_to_list[0] == "refill":
        capacity_liters += int(command_to_list[1])
    else:
        if int(command_to_list[0]) <= capacity_liters:
            capacity_liters -= int(command_to_list[0])
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")
    command = input()

print(f"{capacity_liters} liters left")