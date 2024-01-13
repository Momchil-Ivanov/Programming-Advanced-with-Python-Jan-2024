n_queries = int(input())

stacked_queries = []

for x in range(n_queries):
    command = input()
    command_list = command.split()
    current_command = command_list[0]

    if current_command == "1":
        current_n = int(command_list[1])
        stacked_queries.append(current_n)
    elif len(stacked_queries) > 0:
        if current_command == "2":
            stacked_queries.pop()
        elif current_command == "3":
            print(max(stacked_queries))
        elif current_command == "4":
            print(min(stacked_queries))

final_list = []

for y in range(len(stacked_queries)):
    final_list.append(str(stacked_queries.pop()))

print(", ".join(final_list))