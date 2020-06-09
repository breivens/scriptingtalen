class Grille:
    def __init__(self, dimension, sequence):
        self.dimension = dimension
        self.openings = set(sequence)
        self.grille = [['O' if (r, c) in self.openings else '#' for c in range(self.dimension)] for r in
                       range(self.dimension)]

    def __str__(self):
        return '\n'.join(map("".join, self.grille))

    def __add__(self, other):
        assert self.dimension == other.dimension, "invalid operation"
        return Grille(self.dimension, self.openings & other.openings)

    def __eq__(self, other):
        return self.openings == other.openings

    def decode(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
        encoded = list(map(list, filter(None, content.split('\n'))))
        return "".join([*(encoded[r][c] for (r, c) in sorted(self.openings))])

    def rotate(self, wijzerzin=True):
        self.openings = {(c, self.dimension - r - 1) if wijzerzin else (self.dimension - c - 1, r) for (r, c) in
                         self.openings}
        self.grille = [['O' if (r, c) in self.openings else '#' for c in range(self.dimension)] for r in
                       range(self.dimension)]
        return self
