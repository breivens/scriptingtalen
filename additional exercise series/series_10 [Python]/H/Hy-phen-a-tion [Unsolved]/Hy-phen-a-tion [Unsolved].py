class Hyphenation:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            self._patterns = tuple(filter(None, file.read().split('\n')))

    @staticmethod
    def to_regex(pattern: str):
        return "".join(
            "" if char.isdigit() else
            char if char.isalpha() else
            '^' if (c, char) == (0, '.') else '$'
            for c, char in enumerate(pattern))

    def patterns(self, word: str):
        from re import search, IGNORECASE
        word = word.lower()
        return {pattern for pattern in self._patterns
                if ''.join(filter(str.isalpha, pattern)) in word
                and search(self.to_regex(pattern), word, IGNORECASE)}

    def split(self, word: str):
        from re import sub, IGNORECASE
        patterns = self.patterns(word)  # get patterns for word
        syllables = '0'.join(f'#{word}#')  # setup string for hyphen patterns
        for pattern in patterns:
            pattern = sub(r'\.', '#', pattern)  # replace .'s with #'s in pattern (for convenience)
            pattern = sub('([a-z#]+)', lambda m: '0'.join(m.group()), pattern)  # insert 0 between letters and #'s
            matcher = sub('[0-9]', '[0-9]', pattern)  # pattern to match string with different number
            # replace numbers in string with numbers in pattern if they're bigger
            syllables = sub(matcher,
                            lambda m: ''.join(
                                [max(m.group()[i], char) if char.isdigit() else m.group()[i]
                                 for i, char in enumerate(pattern)]),
                            syllables,
                            flags=IGNORECASE)
        syllables = sub('[0-9]', lambda m: '-' if int(m.group()) % 2 else '', syllables).strip('-#')  # insert hyphens
        return ''.join(['' if char == '-' and i in {1, len(syllables) - 2} else char  # remove abundant hyphens
                        for i, char in enumerate(syllables)])
