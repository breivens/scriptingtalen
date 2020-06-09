from itertools import groupby


class Collection:
    def __init__(self, sequence):
        assert (isinstance(sequence, (list, tuple, set)) and all(
            isinstance(item, int) or (isinstance(item, (list, tuple)) and len(item) == 2) for item in
            sequence)), "invalid collection"
        self.seq = sequence
        self.nums = self.numbers()
        self.nf = self.normalform()

    def __str__(self):
        return str(self.nf)

    def __repr__(self):
        return f"Collection({self})"

    def __len__(self):
        return len(self.nums)

    def __and__(self, other):
        return Collection(self.nums & other.nums)

    def __or__(self, other):
        return Collection(self.nums | other.nums)

    def __sub__(self, other):
        return Collection(self.nums - other.nums)

    def __xor__(self, other):
        return Collection(self.nums ^ other.nums)

    def __eq__(self, other):
        return self.nums == other.nums

    def __ne__(self, other):
        return self.nums != other.nums

    def __lt__(self, other):
        return self.nums < other.nums

    def __le__(self, other):
        return self.nums <= other.nums

    def __gt__(self, other):
        return self.nums > other.nums

    def __ge__(self, other):
        return self.nums >= other.nums

    def numbers(self):
        numbers = set()
        for item in self.seq:
            if isinstance(item, (list, tuple)):
                start, stop = item
                numbers.update(set(range(start, stop + 1)))
            else:
                numbers.add(item)
        return numbers

    def normalform(self):
        return list(self.grouper_n_getter(self.nums))

    @staticmethod
    def grouper_n_getter(collection):
        for group in groupby(enumerate(sorted(collection)), lambda l: l[1] - l[0]):
            g = list(group[1])
            start, stop = g[0][1], g[-1][1]
            yield start if start == stop else [start, stop]

