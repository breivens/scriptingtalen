class Protein:
    def __init__(self, sequence: list, configuration=None):
        length = len(sequence)
        assert length == int(length ** .5) ** 2, "invalid initial state"
        self.dimension = int(length ** .5)
        self.state = [sequence[i:i + self.dimension] for i in range(0, length, self.dimension)]
        self.folds = list()
        if configuration:
            self.fold(configuration)

    def __str__(self):
        from itertools import chain, zip_longest
        lines = [[('-' if i in (0, self.dimension) else ' ') * 4] * self.dimension for i in range(self.dimension + 1)]
        numbers = ["other other".join([str(item).center(4) for item in row]).split('other') for row in self.state]

        for (r1, c1, r2, c2) in self.folds:
            if r1 == r2:
                numbers[r1][2 * c1 + 1] = '|'
            if c1 == c2:
                lines[r1 + 1][c1] = '----'

        grid = [f"|{''.join(row)}|" if i % 2 else f"+{'+'.join(row)}+"
                for i, row in enumerate(chain(*zip_longest(lines, numbers, fillvalue=None))) if row]

        return "\n".join(map("".join, grid))

    def fold(self, configuration=None):
        if configuration:
            for (r1, c1, r2, c2) in configuration:
                assert (abs(r1 - r2), abs(c1 - c2)) in ((0, 1), (1, 0)), "invalid configuration"
                for i in (r1, c1, r2, c2):
                    assert -1 < i < self.dimension, "invalid configuration"
            self.folds = configuration

    def bindingenergy(self):
        return sum(self.state[r1][c1] * self.state[r2][c2] for (r1, c1, r2, c2) in self.folds) if self.folds else 0
