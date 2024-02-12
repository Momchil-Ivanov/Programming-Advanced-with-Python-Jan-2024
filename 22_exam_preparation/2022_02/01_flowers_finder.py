from collections import deque

rose_string = 'rose'
tulip_string = 'tulip'
lotus_string = 'lotus'
daffodil_string = 'daffodil'

rose_found = False
tulip_found = False
lotus_found = False
daffodil_found = False

vowels = deque([str(el) for el in input().split()])
consonants = deque([str(el) for el in input().split()])

while vowels and consonants:
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()

    if first_vowel in rose_string:
        rose_string = rose_string.replace(first_vowel, "")
        if rose_string == '':
            rose_found = True
            break
    if first_vowel in tulip_string:
        tulip_string = tulip_string.replace(first_vowel, "")
        if tulip_string == '':
            tulip_found = True
            break
    if first_vowel in lotus_string:
        lotus_string = lotus_string.replace(first_vowel, "")
        if lotus_string == '':
            lotus_found = True
            break
    if first_vowel in daffodil_string:
        daffodil_string = daffodil_string.replace(first_vowel, "")
        if daffodil_string == '':
            daffodil_found = True
            break

    if last_consonant in rose_string:
        rose_string = rose_string.replace(last_consonant, "")
        if rose_string == '':
            rose_found = True
            break
    if last_consonant in tulip_string:
        tulip_string = tulip_string.replace(last_consonant, "")
        if tulip_string == '':
            tulip_found = True
            break
    if last_consonant in lotus_string:
        lotus_string = lotus_string.replace(last_consonant, "")
        if lotus_string == '':
            lotus_found = True
            break
    if last_consonant in daffodil_string:
        daffodil_string = daffodil_string.replace(last_consonant, "")
        if daffodil_string == '':
            daffodil_found = True
            break

if rose_found or lotus_found or tulip_found or daffodil_found:
    found_word = ''
    if rose_found:
        found_word = 'rose'
    elif lotus_found:
        found_word = 'lotus'
    elif tulip_found:
        found_word = 'tulip'
    elif daffodil_found:
        found_word = 'daffodil'
    print(f'Word found: {found_word}')
else:
    print(f'Cannot find any word!')

if vowels:
    print(f'Vowels left: {" ".join([str(el) for el in vowels])}')

if consonants:
    print(f'Consonants left: {" ".join([str(el) for el in consonants])}')
