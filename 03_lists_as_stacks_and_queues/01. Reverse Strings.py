input_text = str(input())
input_text_to_list = []
new_text = str()
for x in range(0, len(input_text)):
    input_text_to_list.append(input_text[x])

while len(input_text_to_list) > 0:
    new_text += input_text_to_list.pop()

print(new_text)