import os

path = os.path.join("15_file_handling", "test.txt")
try:
    os.remove("test.txt")
except FileNotFoundError:
    print('File is already deleted')