from collections import deque

string_expression = input().split()

number_queue = deque()

for symbol in range(0, len(string_expression)):
    current_symbol = string_expression[symbol]
    if current_symbol == "*":
        while len(number_queue) > 1:
            value = number_queue.popleft()
            number_queue[0] *= value
    elif current_symbol == "+":
        while len(number_queue) > 1:
            value = number_queue.popleft()
            number_queue[0] += value
    elif current_symbol == "-":
        while len(number_queue) > 1:
            value = number_queue.pop()
            number_queue[0] -= value
    elif current_symbol == "/":
        while len(number_queue) > 1:
            value = number_queue.pop()
            number_queue[0] /= value
            number_queue[0] = int(number_queue[0])
    else:
        number_queue.append(int(current_symbol))

print(number_queue[0])