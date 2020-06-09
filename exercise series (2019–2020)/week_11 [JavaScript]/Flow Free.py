class FlowFree:
    def __init__(self, rows: int, columns: int, points: list or tuple):
        self.rows, self.columns = rows, columns

        assert len(points) % 2 == 0 and len(points) == len(set(points)) and all(
            self.is_position(r, c) for (r, c) in points), "invalid configuration"

        self.grid = [['.'] * self.columns for _ in range(self.columns)]
        for i, ((r1, c1), (r2, c2)) in enumerate(zip(*[iter(points)] * 2)):
            self.grid[r1][c1] = self.grid[r2][c2] = chr(65 + i)

    def __str__(self):
        return '\n'.join(map(''.join, self.grid))

    def is_position(self, r, c):
        return -1 < r < self.rows and -1 < c < self.columns

    def pipeline(self, position: list or tuple, directions: str):
        seq, (sr, sc) = [position], position
        directions = directions.upper()

        assert (self.is_position(sr, sc)
                and self.grid[sr][sc].isalpha()
                and set(directions) <= {'U', 'D', 'R', 'L'}), "invalid pipeline"

        for char in directions:
            (r, c,), (x, y) = seq[-1], {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L': (0, -1)}[char]
            r, c = r + x, c + y
            assert (self.is_position(r, c)
                    and self.grid[r][c] in ('.', self.grid[sr][sc])
                    and (sr, sc) != (r, c)), "invalid pipeline"

            seq.append((r, c))
        er, ec = seq[-1]
        assert self.grid[sr][sc] == self.grid[er][ec], "invalid pipeline"
        return seq

    def connect(self, position: list or tuple, directions: str):
        prev_char, pipeline = None, self.pipeline(position, directions)

        for i, char in enumerate(directions.upper()):
            if prev_char:
                r, c = pipeline[i]
                if char == prev_char:
                    self.grid[r][c] = {'U': '|', 'D': '|', 'R': '━', 'L': '━'}[char]
                else:
                    self.grid[r][c] = {'UR': '┏', 'LD': '┏', 'UL': '┓', 'RD': '┓',
                                       'RU': '┛', 'DL': '┛', 'LU': '┗', 'DR': '┗'}[prev_char + char]
            prev_char = char
        return self

    def is_completed(self):
        from itertools import chain
        return '.' not in chain(*self.grid)


game = FlowFree(5, 5, [(0, 1), (3, 0), (0, 2), (4, 0), (0, 3), (4, 3), (1, 3), (2, 2), (4, 2), (3, 3)])
print(game.connect((1, 3), "dl").connect((4, 2), "UR").connect((0, 1), "lddd").connect((0, 2), "dldddl")
      .connect([0, 3], "rddddl"))
print(game.is_completed())
