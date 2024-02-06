from collections import deque


def list_manipulator(nums: list, command: str, location: str, *values):
    nums = deque(nums)
    if command == 'add':
        if location == 'beginning':
            nums.extendleft(values[::-1])
        elif location == 'end':
            for value in values:
                nums.append(value)
    elif command == 'remove':
        if location == 'beginning':
            if values:
                for value in range(values[0]):
                    nums.popleft()
            else:
                nums.popleft()
        elif location == 'end':
            if values:
                for value in range(values[0]):
                    nums.pop()
            else:
                nums.pop()
    return list(nums)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))