from copy import deepcopy


# noinspection Duplicates
class Maze:
    def __init__(self, path):
        with open(path, "r") as f:
            content = f.read()
        self._s_maze = list(map(lambda l: list(l.strip()), filter(None, content.split("\n"))))
        self._r_maze = list(map(lambda l: [{" ": 0., "-": 0., "+": 1., "#": -1.}.get(c, "") for c in l], self._s_maze))
        self._start, self._end = self._get_start_end()
        self._visited = [self._start]
        self._step = 0

    def __str__(self):
        temp = deepcopy(self._s_maze)
        for (r, c) in self.path():
            if (r, c) not in (self._start, self._end):
                temp[r][c] = "~"
        return "\n".join(map("".join, temp))

    def __repr__(self):
        return "\n".join(map(lambda l: " ".join(f"{c:.3f}" if c > -1 else "#####" for c in l), self._r_maze))

    def _get_start_end(self):
        start, end = None, None
        for r, row in enumerate(self._s_maze):
            if "+" in row:
                start = r, row.index("+")
            if "-" in row:
                end = r, row.index("-")
            if start and end:
                break
        return start, end

    def _get_surrounding_cells(self, pos):
        r, c = pos
        return {(r - 1, c): self._r_maze[r - 1][c],
                (r, c + 1): self._r_maze[r][c + 1] if c + 1 < len(self._r_maze[r]) else -1,
                (r + 1, c): self._r_maze[r + 1][c] if r + 1 < len(self._r_maze) else -1,
                (r, c - 1): self._r_maze[r][c - 1]}

    def next_level(self, pos, debit):
        assert 0 <= debit <= 1, "invalid debit"
        r, c = pos
        cell = self._r_maze[r][c]
        if pos in (self._start, self._end) or cell < 0:
            return cell
        return cell + debit * sum(sc - cell for sc in self._get_surrounding_cells(pos).values() if sc >= 0)

    def simulate_level(self, debit, steps=1):
        assert 0 <= debit <= 1, "invalid debit"
        for _ in range(steps):
            self._step += 1
            visited = {}
            for cell in self._visited:
                for sc, sc_val in self._get_surrounding_cells(cell).items():
                    if sc_val >= 0:
                        visited[sc] = self.next_level(sc, debit)
            for (r, c), value in visited.items():
                self._r_maze[r][c] = value
                if (r, c) not in self._visited:
                    self._visited.append((r, c))
        return self

    def path(self):
        route = [self._start]
        lowest_cell, lowest_val = self._start, 1.0
        while len(route) < self._step + 2:
            for sc, sc_val in self._get_surrounding_cells(lowest_cell).items():
                if sc == self._end:
                    return route + [sc]
                if -1 < sc_val < lowest_val:
                    lowest_cell, lowest_val = sc, sc_val
            route.append(lowest_cell)
        return route


d = Maze('doolhof_01.txt')
print(repr(d.simulate_level(.2, 1000)))

