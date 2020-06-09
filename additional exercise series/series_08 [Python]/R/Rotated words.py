def rotation(word: str, count: int) -> str:
    count %= 26
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotated = alphabet[count:] + alphabet[:count]
    return word.translate(str.maketrans(alphabet, rotated))


def wordstem(word: str, beginletter='a') -> str:
    count = 26 - ord(word[0]) + ord(beginletter)
    return rotation(word, count)


def rotatedWords(words: list) -> set:
    from collections import defaultdict
    stems = defaultdict(list)
    for word in words:
        stem = wordstem(word)
        stems[stem] = sorted(stems[stem] + [word])
    return {tuple(item) for item in stems.values() if len(item) != 1}
