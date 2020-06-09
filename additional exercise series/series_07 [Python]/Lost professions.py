def next_letter(letters: str, word: str):
    letters, word = letters.upper(), word.upper()
    if word.count(letters) == 1 and not word.endswith(letters):
        return word[word.index(letters) + len(letters)]
    return ''


def extend(letters: str, words: list):
    letters = letters.upper()
    for i, word in enumerate(words):
        if n := next_letter(letters[i + 1:], word):
            letters += n
        else:
            return ''
    return letters


def profession(words: list, length=2):
    start, words = words[0], words[1:]
    for i in range(len(start) - 1):
        if profession := extend(start[i:i + length], words):
            return profession
    return ''


print(profession(['OPERATOR', 'HERDSMAN', 'WONDERFUL', 'FURNACE', 'HELIUM', 'PALINDROME', 'PAPERBACK']))
