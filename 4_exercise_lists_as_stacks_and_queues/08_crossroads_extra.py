from collections import deque

green_light_duration_seconds = int(input())
free_window_duration_seconds = int(input())

cars = deque()
n_cars_passed = 0

command = input()

while command != "END":
    if command == "green" and cars:
        green_light_seconds_left = green_light_duration_seconds
        for x in range(0, len(cars)):
            current_car = cars[0]
            if len(current_car) < green_light_seconds_left:
                green_light_seconds_left -= len(current_car)
                n_cars_passed += 1
                cars.popleft()
            else:
                last_chance_seconds = green_light_seconds_left + free_window_duration_seconds
                if len(current_car) <= last_chance_seconds:
                    n_cars_passed += 1
                    cars.popleft()
                    break
                else:
                    print(f"A crash happened!")
                    print(f"{current_car} was hit at {current_car[last_chance_seconds]}.")
                    quit()
    else:
        cars.append(command)
    command = input()

print(f"Everyone is safe.")
print(f"{n_cars_passed} total cars passed the crossroads.")