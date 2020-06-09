class BuzzBingo:
    def __init__(self, dimension, sequence):
        assert dimension ** 2 == len(sequence), "invalid card"
        self.cancelled = list()
        self.crosses = [['-'] * dimension for _ in range(dimension)]
        self.card = list((map(list, zip(*[iter(sequence)] * dimension))))

    def __repr__(self):
        return "\n".join(map("".join, self.crosses))

    def cancelWord(self, word):
        assert word not in self.cancelled, f"{word} was already cancelled"
        for r, row in enumerate(self.card):
            if word in row:
                c = row.index(word)
                self.cancelled.append(word)
                self.crosses[r][c] = 'x'
                return r, c
        raise AssertionError(f"{word} not found on card")

    def cancelWords(self, words):
        return [self.cancelWord(word) for word in words]

    def won(self):
        return {'x'} in list(map(set, self.crosses)) + list(map(set, zip(*self.crosses)))
