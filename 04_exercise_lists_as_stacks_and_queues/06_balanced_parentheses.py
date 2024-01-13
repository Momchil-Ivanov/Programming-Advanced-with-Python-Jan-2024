from collections import deque

expression = input()

expression_list = deque()

for char in expression:
    expression_list.append(char)

if len(expression_list) % 2 != 0:
    print("NO")
    quit()

while expression_list:
    if (expression_list[0] == "{" and expression_list[1] == "}") or\
        (expression_list[0] == "[" and expression_list[1] == "]") or \
        (expression_list[0] == "(" and expression_list[1] == ")"):
        expression_list.popleft()
        expression_list.popleft()
    elif (expression_list[0] == "{" and expression_list[len(expression_list) - 1] == "}") or \
            (expression_list[0] == "[" and expression_list[len(expression_list) - 1] == "]") or \
            (expression_list[0] == "(" and expression_list[len(expression_list) - 1] == ")"):
        expression_list.popleft()
        expression_list.pop()
    else:
        print("NO")
        quit()

print("YES")