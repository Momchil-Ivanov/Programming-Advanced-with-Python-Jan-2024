file = open('numbers.txt')

sum = 0

for line in file.readlines():
    sum += int(line)

print(sum)