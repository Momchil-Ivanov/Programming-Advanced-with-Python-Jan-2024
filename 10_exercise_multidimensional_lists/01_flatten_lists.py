from collections import deque

input_string_to_list = input().split('|')
final_list = deque()
for line in input_string_to_list:
    line_list = line.split(" ")
    for el in range(0 , len(line_list)):
        line_list[el] = line_list[el].replace(" ","")
    line_list = [x for x in line_list if x]
    final_list.appendleft(line_list)

for el in range(len(final_list)):
    for item in final_list[el]:
        print(f"{item}", end=" ")