class Grid:
    def __init__(self, arg: str or list or tuple):
        if isinstance(arg, str):
            with open(arg, 'r', encoding='utf-8') as file:
                self.grid = [[int(num) for num in row.split()] for row in file.read().split('\n') if row]
        else:
            self.grid = arg
        assert isinstance(self.grid, (list, tuple)) and len(set(map(len, self.grid)) - {0}) == 1, "invalid grid"

    def largest(self):
        return max(map(max, self.grid))

    def smallest(self):
        return min(map(min, self.grid))

    def __str__(self):
        width = max(len(str(self.smallest())), len(str(self.largest())))
        return '\n'.join([" ".join([str(column).rjust(width) for column in row]) for row in self.grid])

    def __add__(self, other):
        assert len(self.grid) == len(other.grid), "different number of rows"
        return Grid([column + other.grid[i] for i, column in enumerate(self.grid)])

    def __sub__(self, other):
        assert len(self.grid[0]) == len(other.grid[0]), "different number of columns"
        return Grid(self.grid + other.grid)

    def sort(self, decreasing=False, columns=False):
        self.grid = self.sorter(decreasing, columns)
        return self

    def sorted(self, decreasing=False, columns=False):
        sorted_grid = self.sorter(decreasing, columns)
        return all(row == sorted_grid[i] for i, row in enumerate(self.grid))

    def sorter(self, decreasing, columns):
        if columns:
            return list(map(list, zip(*[sorted(row, reverse=decreasing) for row in zip(*self.grid)])))
        return [sorted(row, reverse=decreasing) for row in self.grid]