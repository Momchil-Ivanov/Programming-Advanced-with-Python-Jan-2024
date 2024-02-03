import string

with open('files/text.txt', 'r') as text_file:
    text = text_file.readlines()

output_file = open('files/output.txt', 'w')

line_num = 1

for row in text:

    letters = len([el for el in row if el in string.ascii_letters])
    punctuation_marks = len([el for el in row if el in string.punctuation])
    output_file.write(f'Line {line_num}: {row[:-1]} ({letters})({punctuation_marks})\n')
    line_num += 1