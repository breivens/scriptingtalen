from csv import reader
from copy import deepcopy


class DrunkenAnt:
    dirs = {'^': (-1, 0), '<': (0, -1), 'v': (1, 0), '>': (0, 1)}  # orthogonal movement
    rots = ('^', '<', 'v', '>')  # indexOf - 1 == 90° turn

    def __init__(self, path):
        with open(path, 'r', encoding='utf-8') as file:
            self.grid = list(reader(file, delimiter=' '))
            self.dimension = len(self.grid)
            self.pos = self.dimension - 1, 0

    def __repr__(self):
        return "\n".join(map(" ".join, self.grid))

    def __str__(self):
        temp, (r, c) = deepcopy(self.grid), self.pos
        temp[r][c] = f"[{temp[r][c]}]"
        return "\n".join("".join(char.center(3) for char in row) for row in temp)
        # "\n".join(map(lambda l: "".join(char.center(3) for char in l), temp))  # same but w/ lambda mapping

    def position(self):
        return self.pos

    def step(self):
        r, c = self.pos  # get ant position
        direction = self.grid[r][c]  # get direction
        x, y = DrunkenAnt.dirs[direction]  # get direction offset
        if -1 < r + x < self.dimension and -1 < c + y < self.dimension:  # if not going out of bounds
            self.pos = r + x, c + y  # move in direction
        self.grid[r][c] = DrunkenAnt.rots[DrunkenAnt.rots.index(direction) - 1]  # rotate last position
        return self.pos

    def steps(self):
        positions = [self.pos]
        while self.pos != (0, self.dimension - 1):
            positions.append(self.step())
        return positions
