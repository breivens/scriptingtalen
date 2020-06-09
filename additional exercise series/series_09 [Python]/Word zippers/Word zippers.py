def readWords(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        wordlist = file.read().split('\n')
    return set(wordlist)


def wordzippers(zipper: str, wordlist: set):
    left_word, middle, right_word = map(str.lower, zipper.split('-'))
    length = len(middle)
    mid_words = [(mid_word.upper()) for mid_word in wordlist if len(mid_word) == length
                 and left_word + mid_word in wordlist and mid_word + right_word in wordlist]
    return f"{left_word}-{','.join(sorted(mid_words)) if mid_words else '???'}-{right_word}"


words = readWords("wordlist.txt")
print(wordzippers('gyne-....-wrote', words))
# 'gyne-TYPE-wrote'
print(wordzippers('hydro-....-writer', words))
# 'hydro-TYPE-writer'
print(wordzippers('java-.....-python', words))
# 'java-???-python'
print(wordzippers('agit-....-wood', words))
# 'agit-PROP-wood'
print(wordzippers('arch-...-thing', words))
# 'arch-SEE-thing'
print(wordzippers('frog-...-puller', words))
# 'frog-LEG-puller'
print(wordzippers('arche-....-wrote', words))
# 'arche-TYPE-wrote'
