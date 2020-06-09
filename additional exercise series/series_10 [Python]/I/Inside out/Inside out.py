WORDS = None
HOMONYMS = None
SYMBOLS = None


class MorseCode:
    def __init__(self, path1: str, path2: str):
        global WORDS, SYMBOLS
        if WORDS == SYMBOLS is None:
            with open(path1, 'r', encoding='utf-8') as f1, open(path2, 'r', encoding='utf-8') as f2:
                from csv import reader
                WORDS = tuple(filter(None, f2.read().split('\n')))
                SYMBOLS = dict(reader(f1, delimiter='\t'))

    @staticmethod
    def set_homonyms():
        global HOMONYMS

        def group_homonyms(homonym_words):
            from itertools import groupby
            from operator import itemgetter
            for morse, words in groupby(sorted(homonym_words), itemgetter(0)):
                yield morse, {word[1] for word in words}

        to_morse = str.maketrans(SYMBOLS)
        homonym_words = [(word.translate(to_morse), word) for word in WORDS]
        HOMONYMS = dict(group_homonyms(homonym_words))

    @staticmethod
    def morse(word: str):
        assert all(char in SYMBOLS for char in word), 'invalid word'
        return ' '.join(SYMBOLS[char] for char in word)

    @staticmethod
    def homonyms(morse: str, re=True):
        if HOMONYMS is None:
            MorseCode.set_homonyms()
        if re:
            morse = morse.replace(' ', '')
        return HOMONYMS.get(morse, set())


class MorseWord:
    def __init__(self, word):
        self.code = MorseCode('morsecode.txt', 'words.txt')
        assert word in WORDS and all(char in SYMBOLS for char in word), 'invalid morse word'
        self.word = word
        self.morse = self.code.morse(self.word)
        self.remorse = self.morse.replace(' ', '')

    def __repr__(self):
        return f'{self.__class__.__name__}({self.word!r})'

    def __str__(self):
        return self.morse

    def __eq__(self, other):
        return self.remorse == other.remorse

    def __add__(self, other):
        concat = self.remorse + other.remorse
        homonyms = self.code.homonyms(concat, re=False)
        assert homonyms, 'invalid operation'
        return MorseWord(min(homonyms))

    def isPalinmorse(self):
        return self.remorse == self.remorse[::-1]

    def __neg__(self):
        inverse = self.remorse.translate(str.maketrans('.-', '-.'))
        homonyms = self.code.homonyms(inverse, re=False)
        assert homonyms, 'invalid operation'
        return MorseWord(min(homonyms))