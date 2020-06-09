class Card:
    ranks = ('ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'knight', 'queen', 'king')
    suits = ('clubs', 'diamonds', 'hearts', 'spades')

    def __init__(self, rank: str, suit: str):
        assert (rank in Card.ranks and suit in Card.suits), "invalid card"
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.__class__.__name__}(rank={self.rank!r}, color={self.suit!r})"

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        if self.rank == other.rank:
            return Card.suits.index(self.suit) < Card.suits.index(other.suit)
        return Card.ranks.index(self.rank) < Card.ranks.index(other.rank)

    def __gt__(self, other):
        if self.rank == other.rank:
            return Card.suits.index(self.suit) > Card.suits.index(other.suit)
        return Card.ranks.index(self.rank) > Card.ranks.index(other.rank)

    def __le__(self, other):
        if self.rank == other.rank:
            return Card.suits.index(self.suit) <= Card.suits.index(other.suit)
        return Card.ranks.index(self.rank) <= Card.ranks.index(other.rank)

    def __ge__(self, other):
        if self.rank == other.rank:
            return Card.suits.index(self.suit) >= Card.suits.index(other.suit)
        return Card.ranks.index(self.rank) >= Card.ranks.index(other.rank)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        return self.rank != other.rank or self.suit != other.suit


def fifthCard(sequence: list or tuple):
    convention = {(0, 2): 1, (0, 1): 2, (1, 2): 3, (2, 1): 4, (1, 0): 5, (2, 0): 6}
    first_card, sequence = sequence[0], sequence[1:]
    order = sequence.index(min(sequence)), sequence.index(max(sequence))
    index = (Card.ranks.index(first_card.rank) + convention[order]) % 13
    return Card(Card.ranks[index], first_card.suit)
