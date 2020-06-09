def hapax(string: str) -> list:
    from re import findall
    words = findall('[a-z]+', string.lower())
    return sorted(word for word in set(words) if words.count(word) == 1)
