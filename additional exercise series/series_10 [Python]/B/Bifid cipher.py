class Bifid:
    def __init__(self, dimension, string):
        assert 2 <= dimension <= 10, "2 <= n <= 10 must apply"
        assert dimension ** 2 == len(string), "number of symbols does not correspond to size grid"
        self.dimension = dimension
        self.grid = list((map(list, zip(*[iter(string)] * dimension))))

    def __str__(self):
        return "\n".join(map("  ".join, self.grid))

    def symbol(self, r, c):
        assert -1 < r < self.dimension and -1 < c < self.dimension, "invalid position in grid"
        return self.grid[r][c]

    def position(self, char):
        assert len(char) == 1, "symbol must consist of 1 character"
        for r, row in enumerate(self.grid):
            if char in row:
                return r, row.index(char)
        raise AssertionError(f"unknown symbol: '{char}'")

    def encode(self, string):
        row, column, encoded = "", "", ""
        for char in string:
            r, c = self.position(char)
            row += str(r)
            column += str(c)
        for (r, c) in zip(*[iter(row + column)] * 2):
            encoded += self.symbol(int(r), int(c))
        return encoded

    def decode(self, string):
        row, column, decoded, mid = "", "", "", len(string)
        for char in string:
            r, c = self.position(char)
            decoded += str(r) + str(c)
        row, column, decoded = decoded[:mid], decoded[mid:], ""
        for (r, c) in zip(row, column):
            decoded += self.symbol(int(r), int(c))
        return decoded


cipher = Bifid(9, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz .,;:?!"\'-()[]{}$=%')
print(cipher.encode('This is a dead parrot!'))
print(cipher.decode('WgwygeexfozQ(%II5D$I}O'))
print(cipher.encode('Defend the east wall of the castle'))
