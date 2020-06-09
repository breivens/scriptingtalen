class CardDressage:
    def __init__(self, rows, columns=None):
        self.rows = rows
        self.columns = columns or rows
        self.cards = list((map(list, zip(*[iter("#" * self.rows * self.columns)] * self.columns))))

    def __repr__(self):
        return "\n".join(map("".join, self.cards))

    def turnCard(self, cardnum):
        assert 1 <= cardnum <= self.rows * self.columns, "invalid card"
        r, c = (cardnum - 1) // self.columns, (cardnum - 1) % self.columns
        for (x, y) in ((0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + x, c + y
            if -1 < nr < self.rows and -1 < nc < self.columns:
                self.cards[nr][nc] = '-' if self.cards[nr][nc] == '#' else '#'

    def turnCards(self, cardnums):
        for cardnum in cardnums:
            self.turnCard(cardnum)

    def won(self):
        return {'-'} == set.union(*map(set, self.cards))

cd = CardDressage(5)
cd.turnCards([18, 13, 9, 11, 21, 24, 12, 7, 17, 5, 4, 6, 19, 23])
print(cd)
print(cd.won())