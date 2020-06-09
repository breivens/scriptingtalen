def lettervalue(letterstring: str):
    length = len(letterstring)
    assert letterstring.isalpha() and length % 2 and length == len(set(letterstring)), "invalid letterstring"
    return {letter.upper(): index - length // 2 for index, letter in enumerate(letterstring)}


def wordvalue(word: str, letterstring: str):
    word, value = word.upper(), lettervalue(letterstring)
    assert set(word) <= set(value), "missing letters"
    return sum([value[letter] for letter in word])


def alignment(sequence: list or tuple, letterstring: str):
    return [wordvalue(word, letterstring) for word in sequence] == list(range(len(sequence)))


def arrange1(sequence: list, letterstring: str):
    sequence.sort(key=lambda word: (wordvalue(word, letterstring), word))


def arrange2(sequence: list or tuple, letterstring: str):
    return tuple(sorted(sequence, key=lambda word: (wordvalue(word, letterstring), word)))
