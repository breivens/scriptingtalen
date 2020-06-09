class Grid:
    def __init__(self, sequence: list):
        length = len(sequence)
        assert length == int(length ** .5) ** 2 == len(set(sequence)) and all(
            isinstance(item, int) for item in sequence), "invalid elements"
        self.dimension = int(length ** .5)
        self.grid = [sequence[i:i + self.dimension] for i in range(0, length, self.dimension)]
        self.selected, self.crossed = set(), set()

    def __str__(self):
        n = len(str(max(map(max, self.grid))))
        return '\n'.join([' '.join([
            ('-' if self.is_crossed_out(r, c) else str(column)).rjust(n)
            for c, column in enumerate(row)])
            for r, row in enumerate(self.grid)])

    def element(self, r: int, c: int):
        assert -1 < r < self.dimension and -1 < c < self.dimension, "invalid position"
        return self.grid[r][c]

    def position(self, integer: int):
        for r, row in enumerate(self.grid):
            if integer in row:
                return r, row.index(integer)
        raise AssertionError("element not found")

    def select(self, integer):
        r, c = self.position(integer)
        assert (r, c) not in self.selected | self.crossed, "invalid selection"
        for i in range(self.dimension):
            self.crossed.add((r, i))
            self.crossed.add((i, c))
        self.crossed.remove((r, c))
        self.selected.add((r, c))
        return self

    def is_crossed_out(self, r, c):
        return (r, c) in self.crossed


grid = Grid([2, 13, 16, 11, 23, 15, 1, 9, 7, 10, 14, 12, 21, 24, 8, 3, 25, 22, 18, 4, 20, 19, 6, 5, 17])
print(grid.select(1).select(3).select(6).select(8).select(11))
