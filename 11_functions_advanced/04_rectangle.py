def rectangle(lenght, width):
    if not isinstance(lenght, int) or not isinstance(width, int):
        return f"Enter valid values!"
    else:
        return f'Rectangle area: {width * lenght}\nRectangle perimeter: {width * 2 + lenght * 2}'


print(rectangle('2', 10))