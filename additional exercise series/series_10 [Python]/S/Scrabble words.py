from collections import UserString


class ScrabbleWord(UserString):
    def __init__(self, word):
        super().__init__(word)
        from re import match
        assert match("^[a-zA-Z]+$", word), "invalid word"
        self.word = word

    def score(self):
        return sum(2 if c in 'dg' else
                   3 if c in 'bcmp' else
                   4 if c in 'fhvwy' else
                   5 if c == 'k' else
                   8 if c in 'jx' else
                   10 if c in 'qz' else
                   1 for c in self.word)
