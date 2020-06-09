class Cave:
    def __init__(self, row_count: list or tuple, column_count: list or tuple,
                 entrance: list or tuple, exit: list or tuple):
        self.rows, self.columns = len(row_count), len(column_count)
        assert (all(0 <= count <= self.columns for count in row_count) and
                all(0 <= count <= self.rows for count in column_count) and
                all(r in (0, self.rows - 1) or c in (0, self.columns - 1)
                    for r, c in (entrance, exit))), "invalid cave map"
        self.row_count = row_count
        self.column_count = column_count
        self.entrance = entrance
        self.exit = exit

    def path(self, sequence: str):
        path = [self.entrance]
        for direction in sequence:
            r, c = path[-1]
            x, y = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}[direction]
            assert -1 < r + x < self.rows and -1 < c + y < self.columns, "collides with edge"
            path.append((r + x, c + y))
        return path

    def passages(self, sequence: str):
        rows, columns = zip(*self.path(sequence))
        return tuple(rows.count(i) for i in range(self.rows)), tuple(columns.count(i) for i in range(self.columns))

    def validPath(self, sequence: str):
        path = self.path(sequence)
        return (path[-1] == self.exit and
                len(path) == len(set(path)) and
                self.passages(sequence) == (self.row_count, self.column_count))