numbers_dictionary = {} # {one: 1}

line = input() # one

while line != "Search":
    number_as_string = line

    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print(f'The variable number must be an integer')
    line = input()

line = input()

while line != "Remove":
    searched = line
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print(f'Number does not exist in dictionary')

    line = input()

line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print(f'Number does not exist in dictionary')
    line = input()

print(numbers_dictionary)