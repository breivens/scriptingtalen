class Maze:
    adjacent = ((0, -1), (-1, 0), (0, 1), (1, 0))

    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            self.symbol_grid = [list(row.strip()) for row in file.read().split("\n") if row]

        self.number_grid = [[{' ': 0., '-': 0., '+': 1., '#': -1.}[cell] for cell in row] for row in self.symbol_grid]
        self.rows, self.columns = len(self.number_grid), len(self.number_grid[0])
        self.entry, self.exit = None, None

        for r, row in enumerate(self.symbol_grid):
            if "+" in row:
                self.entry = r, row.index("+")
            if "-" in row:
                self.exit = r, row.index("-")
            if self.entry and self.exit:
                break
        assert self.entry and self.exit, "no entry and/or exit"

    def __repr__(self):
        return '\n'.join(
            [' '.join(['#' * 5 if cell < 0 else f'{cell:.3f}' for cell in row]) for row in self.number_grid])

    def __str__(self):
        path = set(self.path()) - {self.entry, self.exit}
        return '\n'.join([''.join(['~' if (r, c) in path else cell for c, cell in enumerate(row)]) for r, row in
                          enumerate(self.symbol_grid)])

    def accessible(self, r: int, c: int):
        return 0 <= r < self.rows and 0 <= c < self.columns and self.number_grid[r][c] >= 0

    def next_level(self, position: tuple, debit: float):
        r, c = position
        if (r, c) in (self.entry, self.exit) or not self.accessible(r, c):
            return self.number_grid[r][c]
        current_level = self.number_grid[r][c]
        return current_level + sum(
            debit * (self.number_grid[r + ar][c + ac] - current_level) for (ar, ac) in self.adjacent if
            self.accessible(r + ar, c + ac))

    def simulate_level(self, debit: float, steps=1):
        for _ in range(steps):
            self.number_grid = [[self.next_level((r, c), debit) for c in range(self.columns)] for r in
                                range(self.rows)]
        return self

    def path(self):
        path, (r, c) = list(), self.entry
        current_level = self.number_grid[r][c]
        previous_level = 1.0 + current_level
        while current_level < previous_level:
            path.append((r, c))
            previous_level = current_level
            current_level, r, c = min((self.number_grid[r + ar][c + ac], r + ar, c + ac) for ar, ac in self.adjacent if
                                      self.accessible(r + ar, c + ac))
        return path
