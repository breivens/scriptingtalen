def letter_value(sequence: str or tuple or list) -> dict:
    if isinstance(sequence, (list, tuple)):
        sequence = ''.join(sequence)
    sequence, length = sequence.upper(), len(sequence)
    assert length % 2 == 0 and length == len(set(sequence)) and sequence.isalpha(), 'invalid letters'
    output = {}
    for i in range(mid := length // 2):
        output[sequence[i]] = i - mid
        output[sequence[-i - 1]] = mid - i
    return output


def word_value(word: str, sequence: str) -> int:
    word, values = word.upper(), letter_value(sequence)
    assert set(word) <= set(values), 'invalid word'
    return sum(values[letter] for letter in word)


def rainbow(words: list or tuple, sequence: str) -> bool:
    assert all(isinstance(word, str) for word in words), 'invalid word'
    return [word_value(word, sequence) for word in words] == list(range(len(words)))


def reflected(words: list or tuple, sequence: str):
    assert all(isinstance(word, str) for word in words), 'invalid word'
    from functools import cmp_to_key

    def cmp(x, y):
        x, y = x.upper(), y.upper()
        if x == y:
            return 0
        xwv, ywv = word_value(x, sequence), word_value(y, sequence)
        if xwv < ywv or (xwv == ywv and x < y):
            return -1
        return 1

    return tuple(sorted(words, key=cmp_to_key(cmp)))
