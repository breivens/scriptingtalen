class Minesweeper:
    def __init__(self, rows=8, columns=8, mines=None):
        assert rows > 1, "field must contain at least two rows"
        assert columns > 1, "field must contain at least two columns"
        self._rows = rows
        self._columns = columns
        self.mines = sorted(mines) if mines else list()

    def __repr__(self):
        return f"{self.__class__.__name__}{self._rows, self._columns, self.mines}"

    def __str__(self):
        return "\n".join(
            ["".join(['*' if (r, c) in self.mines else str(self.nearbyMines(r, c))
                      for c in range(self._columns)]) for r in range(self._rows)])

    def rows(self):
        return self._rows

    def columns(self):
        return self._columns

    def isMine(self, r, c):
        assert -1 < r < self._rows and -1 < c < self._columns, f"invalid position {r, c}"
        return (r, c) in self.mines

    def addMine(self, r, c):
        self.mines.append((r, c))

    def eraseMine(self, r, c):
        self.mines.remove((r, c))

    def nearbyMines(self, r, c):
        return sum(1 for (dr, dc) in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
                   if -1 < r + dr < self._rows and -1 < c + dc < self._columns and self.isMine(r + dr, c + dc))


field = Minesweeper(4, 5, [(0, 0), (1, 2)])
print(field)
