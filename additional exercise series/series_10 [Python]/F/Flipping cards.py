class Cards:
    def __init__(self, cards):
        from re import match
        assert (all(bool(match('^([jqka2-9]|10)[cdhs]$', card.lower())) for card in cards)
                and len(cards) == len(set(map(str.lower, cards)))), 'invalid cards'
        self.cards = cards

    def __str__(self):
        return ' '.join(['**' if card.islower() else card for card in self.cards])

    def haswon(self):
        return set(self.cards) == {'><'}

    def islands(self):
        return sum(1 for island in ''.join(self.cards).split('><') if island)

    def remove(self, val: str or int):
        if isinstance(val, str):
            val, lowered_cards = val.lower(), [card.lower() for card in self.cards]
            assert val in lowered_cards, "invalid card"
            index = lowered_cards.index(val)
        else:
            assert isinstance(val, int) and -1 < val < len(self.cards), 'invalid card'
            index = val

        assert self.cards[index].isupper(), 'invalid card'

        self.cards[index] = '><'
        if index - 1 > -1:  # left
            self.cards[index - 1] = self.cards[index - 1].swapcase()
        if index + 1 < len(self.cards):  # right
            self.cards[index + 1] = self.cards[index + 1].swapcase()
        return self
