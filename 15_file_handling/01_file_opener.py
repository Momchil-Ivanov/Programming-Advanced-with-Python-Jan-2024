import os

file_name = 'text.txt'

try:
    file = open(file_name)
    print(f'File found')
except FileNotFoundError:
    print(f'File is not found')