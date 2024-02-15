from collections import deque


def best_list_pureness(*parameters):
    list_of_numbers = list(parameters[0])
    k_number = int(parameters[1])
    deque_of_numbers = deque(list_of_numbers)
    max_sum = 0
    best_rotation = 0
    for rotation in range(0, k_number):
        current_sum = 0
        for index in range(len(deque_of_numbers)):
            current_sum += index * deque_of_numbers[index]
        if current_sum > max_sum:
            max_sum = current_sum
            best_rotation = rotation
        deque_of_numbers.rotate(1)

    return f'Best pureness {max_sum} after {best_rotation} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
