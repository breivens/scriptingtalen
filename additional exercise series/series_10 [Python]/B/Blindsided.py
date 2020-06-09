class Pile:
    def __init__(self, deck):
        self.deck = deck.copy()

    def __str__(self):
        return " ".join(card if card[-1].isupper() else "**" for card in self.deck)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.deck})"

    def __eq__(self, other):
        return self.faceUp() == other.faceUp()

    def faceUp(self):
        return sum(1 for card in self.deck if card[-1].isupper())

    def split(self, n=None):
        if n is None:
            n = self.faceUp()
        return Pile(self.deck[:n]), Pile(self.deck[n:])

    def flip(self, arg=None):
        if arg is None:
            arg = tuple(range(len(self.deck)))
        if isinstance(arg, int):
            self.deck[arg] = self.deck[arg].swapcase()
        elif isinstance(arg, (tuple, list, set)):
            for i in arg:
                self.deck[i] = self.deck[i].swapcase()
        return self
