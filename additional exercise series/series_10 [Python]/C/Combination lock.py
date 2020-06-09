class CombinationLock:
    def __init__(self, sequence, maxvalue=9):
        assert sequence and all(0 <= disc <= maxvalue for disc in sequence), "invalid combination"
        self.sequence, self.max, self.disc_count = tuple(sequence), maxvalue, len(sequence)
        self.combination = [0] * self.disc_count

    def __repr__(self):
        return f"{self.__class__.__name__}({self.sequence}, maxvalue={self.max})"

    def __str__(self):
        return "-".join(map(str, self.combination))

    def rotate(self, discs, count):
        if not isinstance(discs, (tuple, int)):
            discs = tuple(discs)
        assert all(-1 < d < self.disc_count for d in discs), "invalid disc"
        for d in discs:
            self.combination[d] = (self.combination[d] + count) % (self.max + 1)

    def open(self):
        return self.sequence == tuple(self.combination)

