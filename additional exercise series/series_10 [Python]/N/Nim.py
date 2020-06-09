class Nim:
    def __init__(self, sequence: list or tuple):
        assert isinstance(sequence, (list, tuple)) and len(sequence) > 1 and all(
            isinstance(item, int) for item in sequence), "invalid heaps"
        self.heaps = list(sequence)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.heaps})"

    def __str__(self):
        return '\n'.join([f"{heap + 1}: {'|' * count}" for heap, count in enumerate(self.heaps)])

    def __add__(self, other):
        from itertools import zip_longest
        return Nim([x + y for x, y in zip_longest(self.heaps, other.heaps, fillvalue=0)])

    def remove(self, heap: int, count: int):
        assert 1 <= heap <= len(self.heaps) and 1 <= count <= self.heaps[heap - 1], "invalid move"
        self.heaps[heap - 1] -= count
        return self

    def won(self):
        return set(self.heaps) == {0}
