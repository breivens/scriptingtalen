class Puzzle:
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            content = [row.strip() for row in file if row.strip()]
        self.grid = content[1:]
        self._dimension = len(self.grid)
        assert content[0].isdigit() and all(self._dimension == len(row) for row in self.grid), "invalid puzzle"
        self._stars = int(content[0])

    @property
    def dimension(self):
        return self._dimension

    @property
    def stars(self):
        return self._stars

    def __setattr__(self, key, value):
        if key in ('dimension', 'stars'):
            raise AttributeError("can't set attribute")
        super().__setattr__(key, value)

    def __str__(self):
        return '\n'.join(map(''.join, self.grid))

    def region(self, r: int, c: int):
        assert -1 < r < self.dimension and -1 < c < self.dimension, "invalid position"
        return self.grid[r][c]

    def positions(self, region: str):
        positions = {(r, c) for r in range(self.dimension) for c in range(self.dimension) if self.grid[r][c] == region}
        assert positions, "invalid region"
        return positions


class Solution():
    def __init__(self, path: str):
        with open(path, 'r', encoding='utf-8') as file:
            self.grid = [row.strip() for row in file if row.strip()]
            self._dimension = len(self.grid)
            self._positions_stars = {(r, c) for r in range(self._dimension) for c in range(self._dimension) if
                                     self.grid[r][c] == '*'}
        assert set.union(*map(set, self.grid)) == {'.', '*'} and all(
            self._dimension == len(row) for row in self.grid), "invalid puzzle"

    @property
    def dimension(self):
        return self._dimension

    @property
    def positions_stars(self):
        return self._positions_stars

    def __setattr__(self, key, value):
        if key in ('dimension', 'positions_stars'):
            raise AttributeError("can't set attribute")
        super().__setattr__(key, value)

    def __str__(self):
        return '\n'.join(map(''.join, self.grid))

    def stars_rows(self):
        rows, _ = zip(*self.positions_stars)
        return [rows.count(i) for i in range(self.dimension)]

    def stars_columns(self):
        _, columns = zip(*self.positions_stars)
        return [columns.count(i) for i in range(self.dimension)]

    def stars_with_neighbours(self):
        return {(r + x, c + y)
                for r, c in self.positions_stars
                for x, y in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
                if -1 < r + x < self.dimension and -1 < c + y < self.dimension
                and self.grid[r + x][c + y] == '*'}

    def stars_regions(self, puzzle: Puzzle):
        stars_regions = dict().fromkeys(set.union(*map(set, puzzle.grid)), 0)
        for r, c in self.positions_stars:
            stars_regions[puzzle.region(r, c)] += 1
        return stars_regions

    def is_valid(self, puzzle: Puzzle):
        return not self.stars_with_neighbours() and set(
            self.stars_rows() +
            self.stars_columns() +
            list(self.stars_regions(puzzle).values())
        ) == {puzzle.stars}