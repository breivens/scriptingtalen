def outside(word):
    return word[0] + word[-1]


def inside(word):
    return word[1:-1]


def issubword(subword, word):
    index = 0
    for letter in subword:
        index = word.find(letter, index)
        if index == -1:
            return False
    return True


"""
def issubword_alt(subword, word):
    from re import match
    pattern, prev_char = "", ""
    for char in subword:
        if char != prev_char:
            pattern += char + ".*"
            prev_char = char
    return bool(match(pattern, word))
"""


def iswandering(subword, word):
    return outside(subword) == outside(word) and issubword(inside(subword), word)


def read_dictionary(path):
    dictionary = {}
    with open(path, 'r', encoding='utf-8') as file:
        for word in file:
            outer = outside(word.strip())
            if outer not in dictionary:
                dictionary[outer] = {}
            dictionary[outer].add(inside(word))
    return dictionary


def wanderings(word, dictionary):
    wanders = set()
    for inner in dictionary.get(outside(word), ""):
        subword = word[0] + inner + word[-1]
        if issubword(subword, word):
            wanders.add(subword)
    return wanders
