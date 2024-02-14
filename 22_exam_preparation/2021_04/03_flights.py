def flights(*args):
    plane_dict = {}
    nums = []
    letters = []
    for info in args:
        if info == 'Finish':
            break
        if str(info).isnumeric():
            nums.append(info)
        else:
            letters.append(info)

    for x in range(len(nums)):
        if letters[x] not in plane_dict:
            plane_dict[letters[x]] = nums[x]
        else:
            plane_dict[letters[x]] += nums[x]

    return plane_dict


# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))