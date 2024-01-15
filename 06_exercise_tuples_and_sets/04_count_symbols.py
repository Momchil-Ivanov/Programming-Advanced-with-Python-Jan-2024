text = input()

text_set = set()

for char in text:
    text_set.add(char)

text_set = sorted(text_set)

for char in text_set:
    print(f"{char}: {text.count(char)} time/s")