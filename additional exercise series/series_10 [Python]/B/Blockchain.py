class Pearson:
    def __init__(self, table=None, combine=lambda h, v: (h + v) % 256):
        permutations = range(256)
        self.table = table or list(permutations)
        self.combine = combine
        if table:
            assert isinstance(table, (list, tuple)) and set(table) == set(permutations), 'invalid table'

    def hash(self, string):
        h = 0
        for char in string:
            h = self.table[self.combine(h, ord(char))]
        return h


class Block:
    def __init__(self, hf=Pearson(), previous=None, index=0, datum='Genesis Block', previous_hash=0):
        self.previous = previous
        self._index = index
        self.datum = datum
        self._previous_hash = previous_hash
        self.hf = hf
        self.hash = self.hf.hash(f'{self.index}{self.datum}{self.previous_hash}')

    @property
    def index(self):
        return self._index

    @property
    def previous_hash(self):
        return self._previous_hash

    def adjoin(self, datum):
        return Block(hf=self.hf, previous=self, index=self.index + 1, datum=datum, previous_hash=self.hash)

    def is_valid(self):
        if self.hash == self.hf.hash(f'{self.index}{self.datum}{self.previous_hash}'):
            return True if self.vorige is None else self.previous.is_valid()
        return False
