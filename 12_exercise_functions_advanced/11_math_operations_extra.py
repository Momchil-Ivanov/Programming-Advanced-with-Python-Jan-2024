def math_operations(*args, **kwargs):
    counter = 0
    for num in args:
        counter += 1
        if counter == 5:
            counter = 1
        if counter == 1:
            kwargs['a'] += num
        elif counter == 2:
            kwargs['s'] -= num
        elif counter == 3:
            if num != 0:
                kwargs['d'] /= num
        elif counter == 4:
            kwargs['m'] *= num

    result = ""
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    for key, value in sorted_result:
        result += f"{key}: {value:.1f}\n"

    return result

print(math_operations(6.0, a=0, s=0, d=5, m=0))