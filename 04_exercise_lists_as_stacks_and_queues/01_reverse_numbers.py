stack_of_numbers = input().split()

reversed_numbers = []

for x in range(0, len(stack_of_numbers)):
    reversed_numbers.append(stack_of_numbers.pop())

print(" ".join(reversed_numbers))
