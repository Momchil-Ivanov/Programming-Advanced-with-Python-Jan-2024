n_commands = int(input())

car_set = set()

for _ in range(n_commands):
    command = input().split(", ")
    action = command[0]
    car = command[1]
    if action == "IN":
        if car not in car_set:
            car_set.add(car)
    elif action == "OUT":
        if car in car_set:
            car_set.remove(car)

if car_set:
    for each_car in car_set:
        print(each_car)
else:
    print(f"Parking Lot is Empty")