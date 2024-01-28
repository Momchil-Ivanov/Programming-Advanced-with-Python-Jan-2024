from typing import List

def print_nums(nums: List[int]) -> None:
    pos_sum = sum(num for num in nums if num > 0)
    neg_sum = sum(num for num in nums if num < 0)

    print(neg_sum)
    print(pos_sum)

    if pos_sum > abs(neg_sum):
        print(f"The positives are stronger than the negatives")
    else:
        print(f"The negatives are stronger than the positives")


numbers = [int(el) for el in input().split()]
result = print_nums(numbers)