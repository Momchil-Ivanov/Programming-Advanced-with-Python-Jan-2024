text_to_copy_paste = input()

try:
    times = int(input())
    print(f'{text_to_copy_paste * times}')
except:
    print(f'Variable times must be an integer')