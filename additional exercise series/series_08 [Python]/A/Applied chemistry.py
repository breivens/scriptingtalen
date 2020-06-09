def isValid(symbol: str, element: str, length=None):
    length = length or len(symbol)
    return length == len(symbol) and symbol.istitle() and issubword(symbol.lower(), element.lower())


def symbols(element: str):
    return {char.upper() + next_char for i, char in enumerate(element[:-1]) for next_char in element[i + 1:]}


def preference(element: str, last=False):
    return max(symbols(element)) if last else min(symbols(element))


def issubword(subword, word):
    index = 0
    for letter in subword:
        index = word.find(letter, index)
        if index == -1:
            return False
    return True