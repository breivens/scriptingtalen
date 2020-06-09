class Alternade:
    def __init__(self, arg):
        if isinstance(arg, str):
            self.words = [arg]
        elif isinstance(arg, list):
            self.words = [*arg]

    def __repr__(self):
        return f'{self.__class__.__name__}({self.words[0] if len(self.words) == 1 else self.words!r})'

    def __str__(self):
        from itertools import chain, zip_longest
        return ''.join(chain(*zip_longest(*self.words, fillvalue='')))

    def __add__(self, other):
        return Alternade(self.words + other.words)
