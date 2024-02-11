def words_sorting(*words):
    words_dict = {}
    total_ascii_sum = 0
    for word in words:
        ascii_sum = 0
        for char in word:
            ascii_sum += ord(char)
        total_ascii_sum += ascii_sum
        words_dict[word] = ascii_sum

    sorted_words_dict = words_dict.copy()

    if total_ascii_sum % 2 != 0:
        sorted_words_dict = dict(sorted(sorted_words_dict.items(), key=lambda kvp: -kvp[1]))
    else:
        sorted_words_dict = dict(sorted(sorted_words_dict.items(), key=lambda kvp: kvp[0]))
    result = ''

    for key in sorted_words_dict.keys():
        result += f'{key} - {sorted_words_dict[key]}\n'

    return result


# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'mythology'
#   ))

# print(
#     words_sorting(
#         'escape',
#         'charm',
#         'eye'
#   ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
