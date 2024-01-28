def fill_the_box(width: int, length: int, height: int, *cubes_quantity):
    volume = width * length * height
    cubes_left = 0
    for x in range(0, len(cubes_quantity)):
        if cubes_quantity[x] == "Finish":
            if cubes_left > 0:
                cubes_left -= volume
                return f'No more free space! You have {cubes_left} more cubes.'
            else:
                return f'There is free space in the box. You could put {volume} more cubes.'
        else:
            if cubes_quantity[x] < volume:
                volume -= cubes_quantity[x]
            else:
                cubes_left += cubes_quantity[x]

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))