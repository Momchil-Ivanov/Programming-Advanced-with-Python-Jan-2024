def palindrome(word: str, index: int):
    limit = len(word) // 2
    if word[index] != word[- index - 1]:
        return f'{word} is not a palindrome'
    if index + 1 < limit:
        return palindrome(word, index + 1)
    else:
        return f'{word} is a palindrome'

print(palindrome("peter", 0))