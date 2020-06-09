def letter_frequencies1(string: str) -> dict:  # slow
    frequencies = dict()
    for char in filter(str.isalpha, string.lower()):
        if char not in frequencies:
            frequencies[char] = 0
        frequencies[char] += 1
    return frequencies


def letter_frequencies2(string: str) -> dict:  # faster
    from collections import Counter
    return dict(Counter(filter(str.isalpha, string.lower())))


def letter_frequencies3(string: str) -> dict:  # fastest
    string = string.lower()
    return {char: string.count(char) for char in filter(str.isalpha, set(string))}


def letter_positions1(string: str) -> dict:  # slow
    string = string.lower()
    return {char: {i for i, x in enumerate(string) if x == char} for char in filter(str.isalpha, set(string))}


def letter_positions2(string: str) -> dict:  # faster
    positions = dict()
    for index, char in enumerate(string.lower()):
        if char.isalpha():
            if char not in positions:
                positions[char] = set()
            positions[char].add(index)
    return positions


def letter_positions3(string: str) -> dict:  # fastest
    from collections import defaultdict
    positions = defaultdict(set)
    for index, char in enumerate(string.lower()):
        if char.isalpha():
            positions[char].add(index)
    return dict(positions)
