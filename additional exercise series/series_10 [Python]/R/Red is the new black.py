class Stack:
    def __init__(self, sequence: list or tuple):
        from re import match
        assert isinstance(sequence, (list, tuple)) and len(sequence) == len(set(sequence)) and all(
            isinstance(card, str) and match("^([JQKA2-9]|10)[CDHS]$", card) for card in sequence), "invalid stack"
        self.cards = list(sequence)

    def __str__(self):
        return " ".join(self.cards)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.cards})"

    def __len__(self):
        return len(self.cards)

    def __add__(self, other):
        return Stack(self.cards + other.cards)

    def draw(self, amount: int):
        assert amount <= len(self), "invalid number of cards"
        drawn, self.cards = self.cards[:amount], self.cards[amount:]
        return Stack(drawn)

    def deal(self):
        from collections import deque
        assert len(self) % 2 == 0, "odd number of cards"

        red, black = deque(), deque()

        for _ in range(len(self) // 2):
            l_card, r_card = self.draw(2).cards
            l_suit, r_suit = l_card[-1], r_card[-1]

            if {l_suit, r_suit} <= {'C', 'S'}:
                black.extendleft((r_card, l_card))
            elif {l_suit, r_suit} <= {'D', 'H'}:
                red.extendleft((r_card, l_card))

        return Stack(tuple(red)), Stack(tuple(black))
