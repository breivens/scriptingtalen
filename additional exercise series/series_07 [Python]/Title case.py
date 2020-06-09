def titleCase(string: str, *words: list) -> str:
    def strip(s: str) -> str:
        return ''.join(c for c in s if c.isalpha() or c == '-')

    def capitalize(s: str) -> str:
        for c in s:
            if c.isalpha():
                return s.replace(c, c.upper(), 1)
        return s

    words = set(words) if words else set()
    return capitalize(' '.join([word if strip(word) in words else capitalize(word) for word in string.split(' ')]))
