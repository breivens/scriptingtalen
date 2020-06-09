def occurrences(word: str):
    from collections import Counter
    return dict(Counter(word.lower()))


def balanced(word: str):
    n = set(occurrences(word).values())
    return len(n) == 1 and next(iter(n)) >= 2
