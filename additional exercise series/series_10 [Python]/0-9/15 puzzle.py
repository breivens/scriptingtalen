class Slidingpuzzle:
    def __init__(self, rows, columns, string):
        assert rows >= 3 and columns >= 3, "puzzle must have at least 3 rows and columns"
        assert len(string) == rows * columns and string.count(" ") == 1, "invalid configuration"
        self.r, self.c = rows, columns  # constants

        self.s = (string.index(" ") // columns, string.index(" ") % columns)  # empty slot
        self.puzzle = list((map(list, zip(*[iter(string)] * columns))))  # puzzle

    def __str__(self):
        return "\n".join(map("".join, self.puzzle))

    def __repr__(self):
        return f"Slidingpuzzle({self.r}, {self.c}, '{''.join(map(''.join, self.puzzle))}')"

    def slide(self, moves):
        directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        for move in moves:
            (sr, sc), (dr, dc) = self.s, directions[move]
            nr, nc = (sr + dr, sc + dc)
            assert -1 < nr < self.r and -1 < nc < self.c, f"invalid direction: {move}"
            self.s = (nr, nc)
            self.puzzle[sr][sc], self.puzzle[nr][nc] = self.puzzle[nr][nc], self.puzzle[sr][sc]
