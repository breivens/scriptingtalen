from copy import deepcopy

# noinspection Duplicates
class Maze:
    def __init__(self, path):
        with open(path, "r") as f:
            content = f.read()
        # string representation
        self._s_maze = list(map(lambda l: list(l.strip()), filter(None, content.split("\n"))))
        # float representation
        self._r_maze = list(map(lambda l: [{" ": 0., "-": 0., "+": 1., "#": -1.}[c] for c in l], self._s_maze))
        # position of start ('+') and end cell ('-')
        self._start, self._end = self._get_start_end()
        # all the visited cells
        self._visited = [self._start]
        # current step
        self._step = 0

    def __str__(self):
        temp = deepcopy(self._s_maze)  # reset maze
        for (r, c) in self.path():  # calculate path and iterate over it
            if (r, c) not in (self._start, self._end):  # replace path cells with '~'
                temp[r][c] = "~"
        return "\n".join(map("".join, temp))  # return in correct format

    def __repr__(self):
        return "\n".join(map(lambda l: " ".join(f"{c:.3f}" if c > -1 else "#####" for c in l), self._r_maze))

    def next_level(self, cell, debit):
        assert 0 <= debit <= 1, "invalid debit"
        r, c = cell  # row, column
        cell_val = self._r_maze[r][c]  # get float value of cell
        if cell in (self._start, self._end) or cell_val < 0:  # start, end and wall cells are constants
            return cell_val
        # x(next) = x + <debit> * ((<up> - x) + (<right> - x) + (<down> - x) + (<left> - x)) only include values >= 0
        return cell_val + debit * sum(sc - cell_val for sc in self._get_surrounding_cells(cell).values() if sc >= 0)

    def simulate_level(self, debit, steps=1):
        assert 0 <= debit <= 1, "invalid debit"
        for _ in range(steps):  # simulate <steps> amount of steps
            self._step += 1
            visited = {}  # dict of visited cells for this iteration
            for cell in self._visited:  # iterate over all visited cells
                for sc, sc_val in self._get_surrounding_cells(cell).items():  # iterate over surrounding cells
                    if sc_val >= 0:  # cannot visit wall cells
                        visited[sc] = self.next_level(sc, debit)  # calculate new float value of cell
            for (r, c), value in visited.items():
                self._r_maze[r][c] = value  # adjust float value
                if (r, c) not in self._visited:  # add new cells
                    self._visited.append((r, c))
        return self

    def path(self):
        path = [self._start]  # path always starts at <start>
        lowest_cell, lowest_val = self._start, 1.0  # <start> is therefore the lowest value
        # loop till path is (<step> + 2) long [derived from exercise -> step 0 : len(path) == 2]
        while len(path) < self._step + 2:
            # iterate over the surrounding cells of the lowest cell
            for sc, sc_val in self._get_surrounding_cells(lowest_cell).items():
                if sc == self._end:  # if at <end>, append <end> and return path
                    path.append(sc)
                    return path
                if -1 < sc_val < lowest_val:  # else check for new lowest cell
                    lowest_cell, lowest_val = sc, sc_val
            path.append(lowest_cell)  # add lowest surrounding cell
        return path

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

    def _get_surrounding_cells(self, cell):
        r, c = cell
        return {(r - 1, c): self._r_maze[r - 1][c],  # up
                (r, c + 1): self._r_maze[r][c + 1] if c + 1 < len(self._r_maze[r]) else -1,  # right
                (r + 1, c): self._r_maze[r + 1][c] if r + 1 < len(self._r_maze) else -1,  # down
                (r, c - 1): self._r_maze[r][c - 1]}  # left
