def numbers_searching(*nums):
    missing_num = 0
    duplicates = []
    for x in range(min(nums), max(nums) + 1):
        if x not in nums:
            missing_num = x
    for el in nums:
        if nums.count(el) > 1 and el not in duplicates:
            duplicates.append(el)

    duplicates.sort()
    return [missing_num, duplicates]



print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))