import re
import os

words = open("words.txt")
input_text = open("input.txt")
output_text_path = os.path.join("text.txt")

with words as file:
    searched_words_as_text = file.read()
    searched_words = searched_words_as_text.split()

with input_text as file:
    content = file.read().lower()

words_count = {}

for searched_word in searched_words:
    pattern = re.compile(rf"\b{searched_word}\b")
    results = re.findall(pattern, content)
    words_count[searched_word] = len(results)

sorted_word_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output_text_path, "a") as file:
    for word, count in sorted_word_count:
        file.write(f'{word}-{count}\n')