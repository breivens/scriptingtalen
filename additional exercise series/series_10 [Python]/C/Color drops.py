class Grid:
    def __init__(self, k, string):
        self.rows, self.columns = len(string) // k, k
        self.grid = list((map(list, zip(*[iter(string.lower())] * self.columns))))
        self.drop_tile = (string.index("*") // k, string.index("*") % k)
        self.blot = [self.drop_tile]

    def __repr__(self):
        return "\n".join(map(" ".join, self.grid))

    def drop(self, color):
        for (br, bc) in self.blot:
            self.grid[br][bc] = color
            for (r, c) in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                nr, nc = br + r, bc + c
                if -1 < nr < self.rows and -1 < nc < self.columns and self.grid[nr][nc] == color.lower():
                    self.grid[nr][nc] = color
                    self.blot.append((nr, nc))
        dr, dc = self.drop_tile
        self.grid[dr][dc] = '*'
        return self

    def drops(self, colors):
        for color in colors:
            self.drop(color)
        return self

    def finished(self, color):
        return {color, '*'} == set.union(*map(set, self.grid))
