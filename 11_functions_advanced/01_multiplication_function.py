def multiply(*args):
    num_result = 1
    for num in args:
        num_result *= num
    return num_result


print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 0, 1000, 5000))